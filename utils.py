"""
Das Modul enthält Hilfsfunktionen, die in verschiedenen Teilen des Projekts verwendet werden können.
In diesem Fall enthält es eine Funktion `print_message`, die eine Nachricht ausgibt,
um den Start und das Ende einer Aufgabe anzuzeigen, mit einer Verzögerung dazwischen.
"""

# Importieren des time-Moduls, um die sleep-Funktion zu verwenden
import time

# Definition der Funktion


def print_message(wait_time=2):
    """
    Prints a message indicating the start and end of a task, with a delay in between.

    Args:
        wait_time (int): The amount of time (in seconds) to wait
        between the start and end messages. Default is 2 seconds.
    """
    print("Task gestartet")
    print(f"Task läuft für {wait_time} Sekunden...")
    time.sleep(wait_time)
    print("Task abgeschlossen")
