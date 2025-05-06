s = input("Nachricht:")
l = len(s)  # ergibt Länge
if s.isalpha():
    print("nur Buchstaben")
if s.isdigit():
    print("nur Ziffern")
if s.islower():
    print("nur Kleinbuchstaben")
if s.isupper():
    print("nur Großbuchstaben")
