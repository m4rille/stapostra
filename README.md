stapostra
=========

Derstandard.at Posting Tracker: überwacht Artikel und meldet gelöschte Postings. Derzeit noch *sehr* experimentell!

Dependencies
------------

* Betriebssystem egal. Linux, Windows, Mac sollten gehen.
* Python (getestet mit 2.7 und 3.3, im Zweifel 2.7 nehmen)
    * [lxml] (http://lxml.de)
    * [Requests] (http://python-requests.org/)

Tip für Windows-User: am einfachsten geht das ganze Setup mit [ActivePython](http://www.activestate.com/activepython) (x86 nehmen, die 64er-Version ist eingeschränkt). Nach installation mit PyPM lxml und requests installieren, das war's.

Anwendung
---------

Auf der Kommandozeile mit der Artikel-ID (siehe URL im Browser) starten:

    python stapostra.py 1371169966891
    
Das Script holt sich dann periodisch alle Postings und meldet, falls welche wieder verschwinden.

Bekannte Einschränkungen
------------------------

* Derzeit ist derstandard.at hartkodiert im Script
* Bei standard.at wird offenbar serverseitiges Caching verwendet, wodurch man öfters einen alten Stand des Forums sieht. Das bedeutet, dass Postings scheinbar verschwinden, dann aber wieder auftauchen. Dieser Effekt wird derzeit nicht berücksichtigt.

