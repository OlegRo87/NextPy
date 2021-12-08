class BankAccount:
    bank_name = "PayPy"

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_balance(self):
        print("Current balance is: ", self.balance)


def main():
    print(BankAccount.bank_name)
    with_prev_money_acc = BankAccount(5000)
    no_prev_money_acc = BankAccount()
    with_prev_money_acc.deposit(1)
    no_prev_money_acc.deposit(1)
    with_prev_money_acc.print_balance()
    no_prev_money_acc.print_balance()


main()
