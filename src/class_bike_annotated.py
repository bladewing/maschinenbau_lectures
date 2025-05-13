class Bike:
    def __init__(self, brand, year, electric):
        self.brand = $\tikzmarknode{brand}{brand}$
        self.year = year
        self.electric = $\tikzmarknode{electric}{electric}$

    def $\tikzmarknode{electrify}{electrify(self):}$
        self.electric = True

    def bike_info(self): $\tikzmarknode{info}$
        return f"{self.year} {self.brand} {'Electric' if self.electric else 'Non-Electric'" 

bike = Bike("Cube", 2023, False)
print(bike.bike_info())
bike.electrify()
print(bike.bike_info())
