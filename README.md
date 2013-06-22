stapostra
=========

Derstandard.at Posting Tracker: überwacht Artikel und meldet gelöschte Postings. Derzeit noch *sehr* experimentell!

Dependencies
------------

* Betriebssystem egal. Linux, Windows, Mac sollten gehen.
* Python (getestet mit 2.7 und 3.3)
    * [lxml] (http://lxml.de)
    * [Requests] (http://python-requests.org/)

Tip für Windows-User: die beiden Python-Module kann man auch mit [inoffiziellen Installern](http://www.lfd.uci.edu/~gohlke/pythonlibs/) runterladen.

Anwendung
---------

Auf der Kommandozeile mit der Artikel-ID (siehe URL im Browser) starten:

    python stapostra.py 1371169966891
    
Das Script holt sich dann periodisch alle Postings und meldet, falls welche wieder verschwinden.
