import numpy as np

temperaturen_celsius = np.array([12.4, 14.7, 26.9])

# Konvertieres jedes Elment in der Liste von Celsius nach Fahrenheit
temperaturen_F = temperaturen_celsius * 9 / 5 + 32

# Kombiniere die Celsius- und Fahrenheit-Temperaturen in einer Liste von Tupeln
ergebnisse = list(zip(temperaturen_celsius.tolist(), temperaturen_F.tolist()))
print(ergebnisse)
