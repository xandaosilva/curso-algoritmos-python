class Person:
    graduation = True

    # Private access
    # __name_var = vale
    # def show_attribute():

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession


    def __str__(self):
        return (f"My name is {self.name}, I'm {self.age} years old and my profession is {self.profession}.")


person_a = Person("Alexandre", 29, "web developer")

print(person_a.__str__())

del person_a

print(person_a.__str__())
