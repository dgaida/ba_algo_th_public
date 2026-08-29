---
layout: page
title: Praktikum
description: Informationen und Downloads zum Online-Marktplatz Praktikum.
nav_order: 4
---

# Online-Marktplatz Praktikum

Dieses Verzeichnis enthält die Codebasis und Dokumentation für das Praktikum im Modul Algorithmik.

## Downloads

- 📦 **[marketplace.zip](/ba_algo_th_public/assets/praktikum/marketplace.zip)** — Startercode für das Praktikum

## Projektübersicht

Der Online-Marktplatz ist eine Python-Anwendung mit einer Tkinter-GUI, die Kernkonzepte aus Datenstrukturen und Algorithmen demonstriert (Mengen, Trees, Heaps, Hashtabellen, Graphen etc.).

## Installation und Abhängigkeiten

Das Projekt benötigt Python (>= 3.11) sowie externe Bibliotheken wie `osmnx` für geografische Distanz- und Routenberechnungen. Sie können die Abhängigkeiten entweder über `pip` oder über eine Anaconda/Conda-Umgebung installieren.

### Option 1: Installation über Pip

1. Stellen Sie sicher, dass Python 3.11 oder neuer installiert ist.  
1. Installieren Sie die erforderlichen Pakete mit `pip`:  

```bash
pip install -r requirements.txt
```

Alternativ können Sie das Paket im Editier-Modus installieren:

```bash
pip install -e .
```

### Option 2: Installation über Anaconda / Conda

Falls Sie Anaconda oder Miniconda verwenden, können Sie die bereitgestellte `environment.yml` nutzen:

1. Erstellen Sie die Conda-Umgebung:  

```bash
conda env create -f environment.yml
```

1. Aktivieren Sie die Umgebung:  

```bash
conda activate marketplace
```

## Aufgabenstellung und Dokumentation

Die vollständige Aufgabenstellung sowie Beschreibungen zu allen drei Teilprojekten finden Sie im Ordner `docs/`:

- [Aufgabenstellung Übersicht](https://github.com/dgaida/ba_algo_th_public/tree/main/assets/praktikum/docs/index.md)  
- [Teilprojekt 1: Projektanalyse und Verständnis](https://github.com/dgaida/ba_algo_th_public/tree/main/assets/praktikum/docs/teilprojekt_1.md)  
- [Teilprojekt 2: Erweiterung der Artikel- und Auktionsverwaltung](https://github.com/dgaida/ba_algo_th_public/tree/main/assets/praktikum/docs/teilprojekt_2.md)  
- [Teilprojekt 3: Freundesverwaltung, Gebotsagenten und Empfehlungssystem](https://github.com/dgaida/ba_algo_th_public/tree/main/assets/praktikum/docs/teilprojekt_3.md)  

## Anwendung starten

Um die Anwendung zu starten, führen Sie im Ordner `praktikum/marketplace` folgenden Befehl aus:

```bash
python gui_marketplace.py
```

Standardmäßig können Sie sich mit Ihrer GM-ID und dem Passwort `abcde` anmelden.

## Tests ausführen

Die Unit-Tests befinden sich im Ordner `tests/`. Sie können mit `pytest` ausgeführt werden:

```bash
pytest tests/
```

