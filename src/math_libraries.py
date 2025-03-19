# importiert das math Modul
import math

minuten = 25

# Der Zugriff auf die Funktionen des Moduls erfolgt über den Modulnamen gefolgt von einem Punkt und dem Funktionsnamen
winkel = minuten / 60 * 2.0 * math.pi
xp = 1.0 + math.sin(winkel)
yp = 1.0 - math.cos(winkel)
