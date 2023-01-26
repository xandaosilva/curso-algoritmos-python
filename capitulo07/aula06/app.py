class Person:
    def __init__(self, name):
        self.name= name

    def say_hello(self):
        print(f"Hello my I'm {self.name}.")


class Hero(Person):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def use_power(self):
        print(f"{self.name} attacks with {self.power} !!!")


hero_a = Hero("Goku", "Kamehameha")

hero_a.say_hello()
hero_a.use_power()
