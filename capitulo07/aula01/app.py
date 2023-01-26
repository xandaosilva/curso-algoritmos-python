class User:
    def __init__(self, name, age, email, profession):
        self.name = name
        self.age = age
        self.email = email
        self.profession = profession


user_a = User("Alexandre", 29, "usera@email.com", "web developer")

print(type(user_a))
print(user_a.name)
print(user_a.age)
print(user_a.email)
print(user_a.profession)
