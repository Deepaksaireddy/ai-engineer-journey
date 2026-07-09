# Coding examples of the concept
#Lists
borrowed = ["Python", "Java", "Oracle"]
borrowed.remove("Java")
borrowed.append("C++")

marks = [90,75,84,100]
print(sum(marks))
print(max(marks))
print(min(marks))

numbers = []
for i in range(10):
    numbers.append(i)
print(borrowed)

#Tuple
book = ("Python", "Java", "Oracle")
print(book)

#sets
book1 = {"Python", "Java", "Oracle", "Oracle", "Java"}
print(book1)

# Dictionary
book = {
    "book_id":101,
    "title":"Python",
    "author":"Deepak",
    "price":450
}
print(book)
print(book["title"])

# Comprehension - a powerful feature
numbers = [i for i in range(10)]
# squares = []
# for i in range(5):
#     squares.append(i*i)
squares = [i*i for i in range(5)]
# comprehension with condition
evens = [i for i in range(20) if i % 2 == 0]
names = ["Deepak","Rahul","Priya"]
upper = [name.upper() for name in names]
print (names)

square = {
    i:i*i
    for i in range(1,5)
}
print (square)