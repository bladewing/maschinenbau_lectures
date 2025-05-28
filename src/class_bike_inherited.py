class Bike:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def bike_info(self):
        return f"{self.year} {self.brand} Non-Electric"


bike = Bike("Cube", 2023)
print(bike.bike_info())
# Output: 2023 Cube Non-Electric


class ElectricBike(Bike):
    def __init__(self, brand, year, battery_capacity):
        super().__init__(brand, year)
        self.battery_capacity = battery_capacity

    def bike_info(self):
        return f"{self.year} {self.brand} Electric with {self.battery_capacity} kWh battery"


ebike = ElectricBike("Cube", 2023, 500)
print(ebike.bike_info())
# Output: 2023 Cube Electric with 500 kWh battery
