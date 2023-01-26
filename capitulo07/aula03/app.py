class Bank():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print(f"Deposit success!!! Your balance is ${self.balance} !!!")

    def bank_transfer(self, value):
        if self.balance <= 0:
            print(f"You can't do transfer bank, because you don't have money. Your balance is ${self.balance} !!!")
        else:
            if self.balance >= value:
                self.balance -= value
                print(f"Bank transfer success!!! Your balance is ${self.balance} !!!")
            else:
                print(f"You can't do transfer bank, because you are trying transfer ${value} and your balance is ${self.balance} !!!")


account_a = Bank("Alistar", 5000.00)

account_a.deposit(5000)
account_a.bank_transfer(7000)
account_a.bank_transfer(7000)
account_a.bank_transfer(3000)
account_a.bank_transfer(3000)
account_a.deposit(1000000)
