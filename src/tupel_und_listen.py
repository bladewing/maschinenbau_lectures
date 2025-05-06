windst_und_richtung = ([3, 5, 6, 3], ["nord", "nordost", "ost", "suedost"])
print(windst_und_richtung)

winddaten = [(3, "nord"), (5, "nordost"), (6, "ost"), (3, "suedost")]
print(winddaten)

winddaten_2 = list(zip(windst_und_richtung[0], windst_und_richtung[1]))
print(winddaten_2)
