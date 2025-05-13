class Bike:
    def __init__(self, brand, year, electric):
        self.brand = brand
        self.year = year
        self.electric = electric

    def electrify(self):
        self.electric = True

    def bike_info(self):
        return f"{self.year} {self.brand} {'Electric' if self.electric else 'Non-Electric'}"


bike = Bike("Cube", 2023, False)
print(bike.bike_info())
bike.electrify()
print(bike.bike_info())
