# Programmablauf Übung

Ein einfaches Python-Programm zur Demonstration eines grundlegenden Programmablaufs.

## Beschreibung

Dieses Projekt zeigt die Struktur eines einfachen Python-Programms mit folgenden Komponenten:

- **main.py**: Der Einstiegspunkt des Programms
- **utils.py**: Ein Hilfemodul mit wiederverwendbaren Funktionen

## Programmablauf

Das Programm führt folgende Schritte aus:

1. Startet das Programm und gibt "Programm gestartet." aus
2. Ruft die Funktion `print_message()` aus dem `utils.py` Modul auf
3. Die Funktion gibt "Task gestartet" aus
4. Wartet 3 Sekunden (die Aufgabe wird simuliert)
5. Gibt "Task abgeschlossen" aus
6. Beendet das Programm mit der Meldung "Programm erfolgreich beendet."

## Ausführung

Um das Programm auszuführen, führen Sie folgenden Befehl aus:

```bash
python main.py
```

## Struktur

```
├── main.py       # Hauptprogramm - ruft Funktionen auf
├── utils.py      # Hilfsfunktionen - enthält die print_message Funktion
└── README.md     # Diese Datei
```

## Lernziel

Diese Übung zeigt:
- Die Aufteilung von Code in Module
- Das Importieren von Funktionen aus anderen Modulen
- Die Verwendung von Parametern und Standardwerten
- Die Verwendung von Verzögerungen im Programmablauf (time.sleep)
