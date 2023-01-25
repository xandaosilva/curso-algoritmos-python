car_a, car_b, car_c = ["BMW", 1000000], ["Ferrari", 100000], ["VW", 10000]
list_cars = [car_a, car_b, car_c]


for car in list_cars:
    print(f"{car[0]} cost ${car[1]:.2f}")
