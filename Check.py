age = int(input("Enter your age: "))

if age >= 0 and age <= 5:
    print("Category: Kids")
elif age >= 6 and age <= 11:
    print("Category: Child")
elif age >= 12 and age <= 19:
    print("Category: Teen")
elif age >= 20:
    print("Category: Adult")
else:
    print("Invalid age")
