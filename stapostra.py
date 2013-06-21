#!/usr/bin/env python
# coding: utf-8
"""
derstandard.at gelöschte-postings-tracker
"""

from __future__ import print_function
from lxml import html
import time
import argparse
import sys

import requests

from datetime import datetime


def get_postings(html_root):
    postings = html_root.xpath('//div[starts-with(@class, "posting")]')
    result = {}
    for p in postings:
        thread = p.xpath(".//div[@class='thread']")[0]
        pid = thread.attrib['id']
        uname = thread.xpath(".//div[@class='uname']/a")[0].text

        textdiv = p.xpath(".//div[@class='txt']")[0]
        text = textdiv.text_content()

        result[pid] = {'name': uname, 'text': text}

    return result


def get_next_url(html_root):
    paging_div = html_root.xpath(".//div[@class='paging']")

    if paging_div:
        fwd_a = paging_div[0].xpath("a[contains(@class,'fwd')]")[0]

        if 'href' in fwd_a.attrib:
            return fwd_a.attrib['href']

    return None


def get_html(path, session=None):
    urlbase = "http://derstandard.at"
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0'}

    if session is None:
        session = requests.session()

    req = session.get(urlbase + path, headers=user_agent)
    req.raise_for_status()
    text = req.text
    return html.document_fromstring(text)


def get_all_article_postings(article_id):
    url = "/" + article_id

    result = {}
    session = requests.session()
    while url:
        root = get_html(url, session)
        result.update(get_postings(root))
        url = get_next_url(root)

    return result


def str_posting(posting):
    return u"'{}' ({})".format(posting['text'], posting['name'])


def monitor_article(article_id, sleep_seconds, break_cond=lambda: True):
    postings = {}
    deleted_postings = []
    while break_cond():
        try:
            new_postings = get_all_article_postings(article_id)
            print("{} postings: {}".format(str(datetime.now()), len(new_postings)))

            for key in postings:
                if not key in new_postings:
                    print("GELÖSCHT: " + str_posting(postings[key]))
                    deleted_postings.append(postings[key])

            postings = new_postings
            time.sleep(sleep_seconds)
        except KeyboardInterrupt:
            print("---- Abbruch")
            print("Gelöschte Postings seit Start:")
            for p in deleted_postings:
                print(str_posting(p))
            sys.exit()


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        description='Derstandard.at Posting Tracker: überwacht Artikel und meldet gelöschte Postings.')
    argparser.add_argument("article_id", help="Artikel-ID aus der URL, typischerweise im Format 123456677")
    argparser.add_argument("-i", "--interval", type=int, help="Intervall zwischen Abfragen, in Sekunden", default=60)
    args = argparser.parse_args()

    monitor_article(args.article_id, args.interval)
