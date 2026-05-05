"""
Einstiegspunkt für das Programm. Hier werden die Funktionen aus utils.py aufgerufen.
In diesem Beispiel wird eine Nachricht gedruckt, dann wird die Funktion print_message
mit einer Wartezeit von 3 Sekunden aufgerufen, bevor eine weitere Nachricht gedruckt wird.
"""

# Importieren der Funktion print_message aus utils.py
from utils import print_message

# Hauptprogramm
# Druckt eine Nachricht, um den Start des Programms anzuzeigen
print("Programm gestartet.")

# Ruft die Funktion print_message auf und übergibt eine Wartezeit von 3
# Sekunden
print_message(wait_time=3)

# Druckt eine Nachricht, um das Ende des Programms anzuzeigen
print("Programm erfolgreich beendet.")
