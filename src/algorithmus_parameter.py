# Funktionsdefinition
def kin_energie(m?\tikzmark{m}?, v?\tikzmark{v}?):
    e = m / 2 * v**2
    return e


# Codeausschnitt mit Aufruf
for masse in range(50, 76, 5):
    for geschw in range(10, 16):
        energie = kin_energie(mas?\tikzmark{mass}?se, ges?\tikzmark{speed}?chw)
        print(masse, geschw, energie)
