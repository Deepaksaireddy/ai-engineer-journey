#if condition
#indentation matters
import hashlib

age = int()
if age >= 18:
    print("Adult")
    print("Can vote")
    print("Can drive")

#if else
if age >= 18 :
    print ('Adult')
else:
    print("Under 18")

#if elif else
marks = 85.5
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")

#using and or
#using input
age = int(input('Please enter your age:'))
salary = int(input('Please Enter your Salary:'))
if age >= 20 and salary >= 45000:
    print('Eligible')
else:
    print('Ineligible')

age = int(input('Please enter your age:'))
salary = int(input('Please Enter your Salary:'))
if age != 24 and salary not in 48000:
    print('Not the threshold')
else:
    print('Correct Threshold')

#Conditions with Variables
#Passsword Validator
username = input(f'Please enter your name:')
username = username.upper()
user_password = input(f'Please enter your password:')
password = 'Deepak@123'
hashed_user_password = hashlib.sha256(user_password.encode()).hexdigest()
hashed_db_password = hashlib.sha256(password.encode()).hexdigest()

if username == 'DEEPAK' and hashed_db_password == hashed_user_password :
    print(f'Welcome, {username}')
else :
    print(f'Wrong Password, {username}')

#------- Activities -------#
# Fizz_buzz
# 3 % num = 0 = Fizz
# 5 % num = 0 = Buzz
# (3 * 5) % num = 0= FizzBuzz

num = int(input("Enter a number :"))

for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif  i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
         print("Buzz")
    else:
        print(i)

# Calculator app

print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
num = int(input("Select a menu:"))

if not num in [1,2,3,4] :
    print("Invalid Selection, Please run again")
elif num == 1:
    num1 = float(input("Enter 1st Value: "))
    num2 = float(input("Enter 2st Value: "))
    print(num1 + num2)
elif num == 2:
    num1 = float(input("Enter 1st Value: "))
    num2 = float(input("Enter 2st Value: "))
    print(num1 - num2)
elif num == 3:
    num1 = float(input("Enter 1st Value: "))
    num2 = float(input("Enter 2st Value: "))
    print(num1 * num2)
elif num == 4:
    num1 = float(input("Enter 1st Value: "))
    num2 = float(input("Enter 2st Value: "))
    print(num1 / num2)

# Temperature Converter
# C - F, F - C
# C - K, K - C

print(" 1. Celsius - Fahrenheit \n 2. Fahrenheit - Celsius \n 3. Celsius - Kelvin \n 4. Kelvin - Celsius")
selection =  int(input("Enter the choice:"))

if not selection in [1,2,3,4] :
    print("Invalid Selection, Please run again")
else:
    temp = float(input("Enter temperature: "))
    if selection == 1:
        print((temp * 9/5) + 32)
    elif selection == 2:
        print((temp - 32) * 5/9)
    elif selection == 3:
        print(temp + 273.15)
    elif selection == 4:
        print(temp - 273.15)