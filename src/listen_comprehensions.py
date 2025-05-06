L1 = list(range(1, 11))
# Generatorfunktion fügt Werte direkt in Liste ein

L2 = list(x / 2 for x in L1)

L3 = list([x, x * x] for x in L2)

L4 = list([x, x * x] for x in L2 if x * x < 5)

print(L1)
print(L2)
print(L3)
print(L4)
