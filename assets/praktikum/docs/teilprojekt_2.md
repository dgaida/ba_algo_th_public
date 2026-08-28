# Teilprojekt 2: Erweiterung der Artikel- und Auktionsverwaltung

[Zurueck zur Uebersicht](index.md)

## Ziele

- Implementierung zusätzlicher Funktionen für die Artikel- und Auktionsverwaltung.  
- Verbesserung der Benutzerfreundlichkeit und Funktionalität.  

## Aufgaben

### 1. Analyse der ADTs und Datenstrukturen

- In welcher Datenstruktur werden alle Gebote auf eine Auktion gespeichert? Warum wird diese Datenstruktur genutzt? (s. `auction.py`)  
- Lassen Sie die aktivste Auktion, d.h. die auf die die meisten Nutzer bieten, als Systemnachricht anzeigen. Nutzen Sie eine geeignete Datenstruktur, die die Auktionen so anordnet, dass die aktivste Auktion in konstanter Zeit abrufbar ist (ein Template ist Ihnen in der Datei `max_heap.py` gegeben). Prüfen Sie alle 30 Sekunden, ob sich die aktivste Auktion geändert hat, und informieren Sie den Nutzer wieder über die Systemnachricht (diese Funktionalität existiert bereits: s. `update_listboxes()` in `gui_marketplace.py`). Die Schwierigkeit ist hier, dass sich die Anzahl der Gebote pro Auktion andauernd ändert und sich damit der Ort, an dem die Auktion in der Datenstruktur gespeichert wird, ebenfalls ändern muss/kann. Sie müssen deshalb zusätzlich eine Hashtabelle nutzen, die den Ort speichert, an dem die Auktion in der eigentlichen Datenstruktur gespeichert ist (s. `max_heap.py` für Details). Es sind ALLE Hilfsmittel zugelassen.  
- Vergleichen Sie die Laufzeit vom Max-Heap mit und ohne die Hashtabelle. Wann lohnt es sich, die Hashtabelle mit dem Max-Heap zu benutzen? Wann sollte man nur einen Max-Heap benutzen?  

### 2. Interaktion und Feedback

- Fügen Sie eine Bewertungsfunktion (1 bis 5 Sterne) hinzu, mit der Nutzer Verkäufer bewerten können. Der am besten bewertete Verkäufer soll alle 30 Sekunden als Systemnachricht angezeigt werden. Es soll die am besten geeignete Datenstruktur gewählt werden. Beachten Sie, dass sich der am besten bewertete Verkäufer während der Laufzeit des Programms verändern kann (s. Ähnlichkeit zu aktivste Auktion oben). In `auctions.py` finden Sie bereits die Methode `get_top_rated_user()`, die den beliebtesten Nutzer liefert. Dieser wird auch bereits als Systemnachricht ausgegeben, s. `update_listboxes()` in `gui_marketplace.py`. Sie sollen lediglich eine bessere Datenstruktur wählen und die Methode `get_top_rated_user()` anpassen (s. TODOs in `auctions.py`).  

### 3. Dokumentation

- Erstellen Sie eine kurze Präsentation, in der Sie die oben gestellten Fragen beantworten und Ihren Code präsentieren.  
- Laden Sie den Code als ZIP-Datei und die Folien als PDF in Ihrer Gruppe hoch. Wir werden uns beide ansehen. Sie müssen es nicht im Praktikum präsentieren.  
