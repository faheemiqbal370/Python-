class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Rupees{amount} deposited.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"rupees{amount} withdrawn.")

    def show_balance(self):
        print(f"Current Balance: rupees{self.balance}")


def main():
    acc = BankAccount()

    while True:
        print("""
              Choose Option

1. Deposit
2. Withdraw
3. Check Balance
0. Exit
""")
        ch = input("Enter choice: ")

        if ch == "1":
            acc.deposit(int(input("Enter amount: ")))

        elif ch == "2":
            acc.withdraw(int(input("Enter amount: ")))

        elif ch == "3":
            acc.show_balance()

        elif ch == "0":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")


main()
