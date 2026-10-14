import json
from pathlib import Path


DATA_FILE = Path("bank_data.json")
INITIAL_BALANCE = 1000.00


def load_balance():
    if not DATA_FILE.exists():
        return INITIAL_BALANCE

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        balance = float(data["balance"])

        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        return balance

    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Warning: Could not load saved balance.")
        print("Starting with the initial balance.")
        return INITIAL_BALANCE


def save_balance():
    data = {
        "balance": round(balance, 2)
    }

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


balance = load_balance()


def show_balance():
    print(f"\nYour current balance is: {balance:.2f} RON")


def deposit_money():
    global balance

    try:
        amount = float(input("Enter deposit amount: ").replace(",", "."))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        balance = round(balance + amount, 2)
        save_balance()

        print(f"Deposit successful! New balance: {balance:.2f} RON")

    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def withdraw_money():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: ").replace(",", "."))

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance = round(balance - amount, 2)
            save_balance()

            print(f"Withdrawal successful! New balance: {balance:.2f} RON")

    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def main():
    while True:
        print("\n===== PYTHON BANK =====")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "0":
            print("Thank you for using Python Bank!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
