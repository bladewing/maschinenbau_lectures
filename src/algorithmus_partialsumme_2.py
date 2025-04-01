import algorithmus_ps_modul

print("Partialsumme P(n) mit Modul")
n = int(input("n:"))
ps = algorithmus_ps_modul.psum(n)
print("P(", n, ")=", ps)
