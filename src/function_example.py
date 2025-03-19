def mittelwert3(a, b, c):
    sum = a + b + c
    mw = sum / 3.0
    return mw


x = float(input("erster Wert:"))
y = float(input("zweiter Wert:"))
z = float(input("dritter Wert:"))

print("Eingegeben wurde:", x, y, z)

m = mittelwert3(x, y, z)

print("Der Mittelwert ist:", m)
