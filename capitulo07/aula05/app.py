class Person:
    def say_hello(self):
        print("Hello")


class Child(Person):
    def say_hello(self):
        print("Hello guys, I'm child.")


child_a = Child()
child_a.say_hello()
