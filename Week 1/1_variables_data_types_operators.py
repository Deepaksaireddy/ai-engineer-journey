#variables
x = 10
name  = "Deepak"
price = 99.99

print (x)
print(type(x))

#Data Types
#string
first = "Deepak"
last = "L"
print(type(first + " " + last))

#int
a = 10
b = -50
c = 1000000
print(type(a))

#float
pi = 3.14159
print(type(price))

#bool
is_logged_in = True
is_admin = False
print(type(is_logged_in))
print(not True)

#complex
comp = 3J+4
print(type(comp))

#type conversion
age = "24"
age = int(age)
print(age + 1)

age = 24
print("Age: " + str(age))

#operators
a = 10
b = 3

print(a + b, 'Addition')
print(a - b, 'Subtraction')
print(a * b, 'Multiplication')
print(a / b, 'Division')
print(a // b, 'Modulo')
print(a ** b, 'Exponent')
print(a % b, 'Floor Division')

#logical operators
print(10 > 5 and 20 > 10)
print(10 > 5 or 20 < 10)

#assignment operator (a1 = a1 - 2)
a1 = 10
a2 = 10
a3 = 10
a4 = 10

a1 -= 2
a2 *= 3
a3 /= 4
a4 %= 2
print(a1, a2, a3, a4)