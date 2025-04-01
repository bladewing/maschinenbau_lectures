a = float(input("Geben Sie die Länge der Seite a ein: "))
b = float(input("Geben Sie die Länge der Seite b ein: "))
c = float(input("Geben Sie die Länge der Seite c ein: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"Der Flächeninhalt des Dreiecks beträgt: {A:.2f}")
else:
    print("Das Dreieck existiert nicht.")