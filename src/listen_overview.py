def calc_fun1(a, b):
    return a + b


temperaturen = [12.4, 13.4, 15.7, 18.9, 23.6, 25.0, 26.7, 25.5]
dritter = temperaturen[2]  # Indizierung einzelnes Element


mischwaren = [45, "Minuten", 17.95, (13, 66), calc_fun1]
print(mischwaren[0], mischwaren[1])  # 1. und 2. Element

e = mischwaren[4](mischwaren[3][0], mischwaren[3][1])
# Aufruf der an Index 4 eingetragenen Funktion mit Argumenten aus Index 3
