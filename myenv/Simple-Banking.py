# Simple Banking System

balance = 0  # Stores the account balance
transactions = []  # Stores transaction history

def check_balance():
    return balance  # Returns the current balance

def deposit(amount):
    global balance  
    balance += amount  # Adds money to balance
    transactions.append(f"Deposited: ${amount}")  # Saves transaction
    return f"Deposited ${amount}. New balance: ${balance}"

def withdraw(amount):
    global balance  
    if amount > balance:
        return "Not enough money!"
    balance -= amount  # Subtracts money from balance
    transactions.append(f"Withdrawn: ${amount}")  # Saves transaction
    return f"Withdrew ${amount}. New balance: ${balance}"

def view_transactions():
    if transactions:  # If there are transactions, print them
        return "\n".join(transactions)
    return "No transactions yet."

while True:

    print('MNB Mohale Mational Bank')
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transactions")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    match choice:
        case '1':
            print(f"Your balance: ${check_balance()}")

        case '2':
            amount = float(input("Enter amount to deposit: "))
            print(deposit(amount))

        case '3':
            amount = float(input("Enter amount to withdraw: "))
            print(withdraw(amount))

        case '4':
            print("\nTransaction History:")
            print(view_transactions())

        case '5':
            print("Exiting program!")
            break

        case _:
            print("Invalid choice. Please enter a number from 1 to 5.")
