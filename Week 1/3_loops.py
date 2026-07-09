# Loops
# for loop
for i in range(5):
    print('Hello, World -',i)

# (start, stop)
for i in range(1, 6):
    print(i)

# (start, stop, jump)
for i in range(10, 20, 2):
    print(i)

# counting back
for i in range(10, 0, -1):
    print(i)

#Sting looping
name = 'Deepak'
for ch in name:
    print(ch)

#advanced
names = ["John", "Mary", "Deepak"]
for i in range(len(names)):
    print(i, names[i])

#-------while Loop -------#
count = 1
while count <= 5:
    print(count)
    count += 1

#dangerous in while loop - creates the infinite loop
# while True:
#     print("Hello")

#------- Break -------#
for i in range(10):
    if i == 5:
        break
    print(i)

#------- Continue -------#
for i in range(5):
    if i == 2:
        continue
    print(i)

#------- Nested loops -------#
for i in range(4):
    for j in range(2):
        print(i, j)

#with variable fib series
def fib(n):
    a,b = 0,1
    for _ in range(n):
        print(a, end= '\n')
        a,b= b,a+b
print(fib(int(input('Give the number for fib'))))

def fibon(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]

    series = [0, 1]

    for _ in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)

    return series

print(fibon(10))

