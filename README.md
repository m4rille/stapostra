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

Warum?
------

Die Foren auf derstandard.at sind zwar nett, aber mitunter von unerklärlichen Löschaktionen betroffen: es verschwinden immer wieder Postings spurlos, ohne wirklich erkennbaren Grund (d.h. keine wüsten Beschimpfungen oder Illegales). Das passiert meistens bei den (wenigen) nicht von der APA übernommenen Artikeln. Ich wollte eine Möglichkeit, sowas zu bemerken - mein Eindruck ist, dass gekränkte Artikelautoren öfters auch harmloseste Kritik löschen. 

Bekannte Einschränkungen
------------------------

* Derzeit ist derstandard.at hartkodiert im Script
* Bei standard.at wird offenbar serverseitiges Caching verwendet, wodurch man öfters einen alten Stand des Forums sieht. Das bedeutet, dass Postings scheinbar verschwinden, dann aber wieder auftauchen. Das Script versucht diesen Effekt auszugleichen, es kann aber sein dass trotzdem Pseudo-Löschungen gemeldet werden.
* Das Ding kann nicht zaubern: Postings die überhaupt nie veröffentlicht werden, kann es auch nicht bemerken. Es findet nur jene, die nach Veröffentlichtung wieder gelöscht werden. Das passiert offenbar immer manuell, entweder auf Zuruf durch den "Melden"-Knopf oder nach Lust und Laune eines Redakteurs(?). 
