#CLass, Objects, Attributes, Methods
#Example 1: Banking
class BankAccount:

    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance =  balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully")
        print(f"Your Current Balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient Balance !")
        else:
            self.balance -= amount
            print(f"An amount of {amount} is withdrawn successfully")
            print(f"Your current Balance is {self.balance}")

    def checkBalance(self):
        print(f"Your Current Balance is {self.balance}")

#Use: this is account opening
account1 = BankAccount(1001, "Deepak", 10000)
# account2 = BankAccount("1002", "Rahul", 10000)

account1.deposit(2000) #deposit
account1.withdraw(1500) #withdrawl
account1.checkBalance() #check balance

#Example 2:
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, increase):
        self.speed += increase
        print(f"Speed increased to {self.speed} Km/H")

    def decelerate(self, decrease):
        self.speed -= decrease
        print(f"Speed decreased to {self.speed} Km/H")

    def display(self):
        print(f"{self.brand} - {self.model} with {self.speed} Km/H")

CarBrand1 = Car("BMW", "x6m", 340)
CarBrand1.decelerate(10)
CarBrand1.display()