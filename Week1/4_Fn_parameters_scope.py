#Functions
def greet():
    print("Hello")

greet() #Function call

#Parameterized Functions
def greet_with_name(name_parameter):
    print(f"Hello {name_parameter} how are you" )

name = input("Please Enter Your name: ")
greet_with_name(name)

#Multiple parameters 1
def add(a, b):
    print(a + b)

add(18,8)

#Multiple parameters
def student(name: str, age: int):
    if age <= 0:
        print(f"Your age is invalid")
    else:
        print(f"{name} is {age} years old")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
student(name , age)

#function with return value
def calculate_tax(price):
    return price * 0.16

print(calculate_tax(float(input("Enter your amount for tax calculation: "))))

#returning multiple values
def calculate(a, b):
    return a+b, a-b

result = calculate(25, 13)
print(result)

def calculate(a, b):
    return a+b, a-b

summ, diff = calculate(25, 13)
print(summ)
print(diff)

#----------Scope----------#
#Local scope - Variable created inside a function
def test():
    x = 100
    print(x)

test()

#Global scope - Variable created outside a function
x = 100
def test():
    print(x)

test()

#local vs global
y = 10
def test():
    y= 20
    print(y)

test()
print(y)

#---------- Variable no of arguments ----------#
# u don't know how many will come
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(10,20,30))

#---------- activities ---------#
# Multiplication of a,b
def multiply(a: int, b:int):
    return(a*b)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print( multiply(num1,num2 ))
