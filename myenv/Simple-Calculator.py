# Functionalities
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

while True:
    print("\nSelect operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    menu = input("Enter a number (1-4 for operations, 5 to exit): ")

    if menu == '5':
        print("Exiting the program.")
        break

    if menu not in ['1', '2', '3', '4']:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid number input. Please enter numeric values.")
        continue

    match menu:
        case '1':
            print(f"Result: {add(num1, num2)}")
        case '2':
            print(f"Result: {subtract(num1, num2)}")
        case '3':
            print(f"Result: {multiply(num1, num2)}")
        case '4':
            print(f"Result: {divide(num1, num2)}")
