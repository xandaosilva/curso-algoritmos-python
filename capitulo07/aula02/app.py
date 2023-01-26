class Car:
    def __init__(self, doors, engine, sunroof, brand, price, tank):
        self.doors = doors
        self.engine = engine
        self.sunroof = sunroof
        self.brand = brand
        self.price = price
        self.tank= tank


    def show_info(self):
        return (f"Car: {self.brand} - Doors: {self.doors} - Engine: {self.engine} - Sunroof: {self.sunroof} - Price: ${self.price:.2f} - Tank: {self.tank}L")


car_a = Car(4, 1, True, "VW", 10000.00, 150)
car_b = Car(4, 1, False, "Fusca", 5000.00, 300)
car_c = Car(4, 1, True, "Renault", 30000.00, 200)
car_d = Car(2, 1, True, "Ferrari", 1000000.00, 500)
car_e = Car(4, 1, True, "BMW", 500000.00, 350)

info_car_a = car_a.show_info()
info_car_b = car_b.show_info()
info_car_c = car_c.show_info()
info_car_d = car_d.show_info()
info_car_e = car_e.show_info()

print(info_car_a)
print(info_car_b)
print(info_car_c)
print(info_car_d)
print(info_car_e)
