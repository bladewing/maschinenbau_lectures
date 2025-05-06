text = "fahrradfahrt"

o = text.find("fahr")  # ergibt 0
p = text.find("rad")  # ergibt 4
q = text.find("bus")  # ergibt -1

p = text.rfind("rad")  # ergibt 7
