class Vehicle:
    def __init__(self, tires, brand):
        self.tires = tires
        self.brand = brand


class Car(Vehicle):
    def __init__(self, tires, brand, sunroof, airbag):
        super().__init__(tires, brand)
        self.sunroof = sunroof
        self.airbag = airbag


class Motorcycle(Vehicle):
    def __init__(self, tires, brand, side_protection):
        super().__init__(tires, brand)
        self.side_protection = side_protection


car_a = Car(4, "Ferrari", True, True)
moto_a = Motorcycle(2, "Suzuki", True)

print(f"{car_a.brand} - Tires:{car_a.tires} - Sunroof: {car_a.sunroof} - Airbag: {car_a.airbag}")
print(f"{moto_a.brand} - Tires:{moto_a.tires} - Side protection: {moto_a.side_protection}")


