def add(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None # Indicate error for clarity

def subtract(x, y):
    try:
        return float(x) - float(y)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None

def multiply(x, y):
    try:    
        return float(x) * float(y)
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def divide(x, y):
    if y == 0:
        print("Error! Division by zero!")
        return None
    else:
        try:
            return float(x) / float(y)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return None

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Exiting calculator. Good bye!")
        break
    else:
        print("Invalid input")
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break

