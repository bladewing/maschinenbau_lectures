a = float(input("Geben Sie a ein: "))
b = float(input("Geben Sie b ein: "))
c = float(input("Geben Sie c ein: "))

d = b**2 - 4*a*c
if d >= 0:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    if d == 0:
        print(f"Eine Lösung: {x1}")
    else:
        print(f"Zwei Lösnugen: {x1} und {x2}")
else:
    print("Keine Lösung")