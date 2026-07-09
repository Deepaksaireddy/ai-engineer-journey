class Employee :

    def __init__(self,emp_id, emp_name, emp_salary):
        self.id = emp_id
        self.name = emp_name
        self.salary = emp_salary

    def increaseSalary(self,amount):
        if amount > 0 :
            self.salary += amount

    def getSalary(self):
        return f"Your Current Salary is {self.salary}"

    def calculateBonus(self):
        pass

class Developer(Employee):
    def calculateBonus(self):
        return self.salary * 0.20

class Manager(Employee):
    def calculateBonus(self):
        return self.salary * 0.35

class Engineer(Employee) :
    def calculateBonus(self):
        return self.salary * 0.25

employees = [
    Developer(100, "Deepak", 25000),
    Manager(101, "Ram", 35000),
    Engineer(102, "Krishna",  28000)
]

for emp in employees:
    print(emp.name)
    print(emp.id)
    print(f"Salary : {emp.getSalary()}")
    print(f"Manager's Bonus : {emp.calculateBonus()}")
    print()

print(employees[0].name)  #or
# emp = employees[1]
# print(emp.name)

#########################################
""" 
For the understanding
1. Encapsulation : self.salary = emp_salary
    def increaseSalary(self,amount):
        if amount > 0 :
            self.salary += amount
    if someone does employees[1].salary = -30000 this is wrong
    so they should use employees[1].increaseSalary(2000)
    
2. Inheritance : 
class Developer(Employee):
class Manager(Employee):
class Engineer(Employee) : 
here employee is brought to different classes instead of duplicating the attributes

3. Abstraction :
We don't know how bonus is calculated but we can get bonus by this function : 
employees[1].calculateBonus()

4. Polymorphism :

for emp in employees:
    print(emp.name)
    print(emp.id)
    print(f"Salary : {emp.getSalary()}")
    print(f"Manager's Bonus : {emp.calculateBonus()}")
    print()

one code but gives more than one results when executed 
"""