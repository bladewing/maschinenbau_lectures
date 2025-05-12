import math

cities = {
    "dresden": (51.049259, 13.73836),
    "leipzig": (51.340333, 12.37475),
    "magdeburg": (52.133333, 11.616667),
    "cottbus": (51.760806, 14.331861),
}

for c in cities:
    print(c, cities[c])

dd_coords = cities["dresden"]
# cities['berlin'] würde hier noch KeyError ergeben
b_coords = cities.get("berlin")  # liefert none

cities["berlin"] = (52.518611, 13.408333)
b_coords = cities["berlin"]  # liefert jetzt ein Tupel


def distance_km(geo_koord_von, geo_koord_nach):
    breite1_rad = geo_koord_von[0] / 180 * math.pi
    laenge1_rad = geo_koord_von[1] / 180 * math.pi
    breite2_rad = geo_koord_nach[0] / 180 * math.pi
    laenge2_rad = geo_koord_nach[1] / 180 * math.pi
    # hier wird gerechnet
    dist_km = 6371 * math.acos(
        math.sin(breite1_rad) * math.sin(breite2_rad)
        + math.cos(breite1_rad)
        * math.cos(breite2_rad)
        * math.cos(laenge2_rad - laenge1_rad)
    )
    return dist_km


for c1 in cities:
    for c2 in cities:
        e = distance_km(cities[c1], cities[c2])
        print(f"Entfernung {c1} - {c2}: {e:.2f} km")
