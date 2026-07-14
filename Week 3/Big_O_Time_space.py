# Practice Examples
# Time complexity
"""O(1) - complexity"""
numbers = [10,20,30,40]
print(numbers[2])

"""O(log n) - complexity"""
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + right//2
        if mid == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

a= [1,2,3,4,5,6,7,8,9,10]
print(binary_search(a, 3))

"""O(n) - complexity"""
numbers = [10,20,30,40]
for num in numbers:
    print(num)

"""O(n log n) - complexity"""
num = [9,5,2,8,1]
num.sort()

"""Space Complexity"""
numbers = [1,2,3,4]
copy = []
for n in numbers:
    copy.append(n)

"""Other Examples"""
#Listing Index
item = numbers[100]
#Time: O(1)
#Space: O(1)

"""Searching Unsorted list"""
target = 25
for num in numbers:
    if num == target:
        break
#Time: O(n)
#Space: O(1)

"""Dictionary lookup"""
student = {
    "id": 101,
    "name": "Deepak"
}
print(student["name"])
# Time: O(1)
# Space: O(1)

"""Creating new list"""
squares = [x * x for x in numbers]
# Time: O(n)
# Space: O(n)

"""nested comparison"""
for a in numbers:
    for b in numbers:
        if a == b:
            print(a)
#Time: O(n²)
#Space: O(1)