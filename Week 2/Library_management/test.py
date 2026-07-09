employee = {
    "name":"John",
    "salary":50000,
    "department":"IT"
}

print(f"{employee.items()}")

names = ["john","sam","alex"]

upper = [name.upper() for name in names]
# upper = names.upper()

print(upper)