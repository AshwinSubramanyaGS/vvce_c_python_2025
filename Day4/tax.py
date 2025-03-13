'''Program to accept name and salary. Check if their salary is >3L and display if they have to pay tax'''

# Accept employee details
name = input("Enter employee's name: ")
salary = float(input("Enter employee's annual salary: "))

# Check if salary is greater than 3,00,000
if salary > 300000:
    print(f"{name} has an annual salary of ₹{salary}.")
    print(f"{name} has to pay taxes.")
else:
    print(f"{name} has an annual salary of ₹{salary}.")
    print(f"{name} does not have to pay taxes.")