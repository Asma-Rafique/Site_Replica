class banks:
    accounts = {}

    def __init__(self):
        print("\n\n ______________wellcome to our banking service______________\n")

    def create_account(self, acc_no, owner, balance):
        if acc_no in self.accounts:
            raise ValueError("account already exist")
        self.accounts[acc_no] = Account(acc_no, owner, balance)

    def get_account(self, acc_no):
        if acc_no in self.accounts:
            return self.accounts.get(acc_no, None)


class Account:

    def __init__(self, acc_no=None, owner=None, balance=0):
        self.account_no = acc_no
        self.owner = owner
        self.balance = balance

    @classmethod
    def set(cls, account, amount):
        return account.deposit(amount)

    @classmethod
    def get(cls, account, amount):
        return account.withdraw(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("sorry you have not the enough money to withdraw")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("please add the amount greater than zero")
        self.balance += amount

    def __str__(self):
        return f"Account({self.account_no}, {self.owner}, Balance: {self.balance})"

# class transactions:
#     def __init__(self,account):
#         self.account=account
#     def


def main():
    banking_sys = banks()
    while True:
        print(" \n Press 1 for Acconut creation")
        print(" \n Press 2 for Deposit Amount")
        print(" \n Press 3 for Withdraw Amount")
        print(" \n Press 4 for Checking Acconut Balance")
        print(" \n Press 5 for Exit")
        option = int(input("\n Enter Your Choice"))
        if option == 1:
            name = input("\n Enter the name of Account Owner\t")
            acc_no = input("\n Enter Account Number\t")
            bal = float(input(
                "\n Enter the Initail amount to add in your account if not then enter 0 amount\t"))
            acc_check = banking_sys.get_account(acc_no)
            if acc_check:
                banking_sys.create_account(acc_no, name, bal)
                print("\n \n Account Created successfully")
            else:
                print("\n Account Already Exist.")
        elif option == 2:
            acc_no = input("\n Enter Account Number\t")
            amount = float(input(
                "\n Enter the amount you want to add in your account\t"))
            acc_check = banking_sys.get_account(acc_no)
            if acc_check:
                account = Account()
                account.set(acc_check, amount)
            else:
                print("\n Account not found.")
        elif option == 3:
            acc_no = input("\n Enter Account Number\t")
            amount = float(input(
                "\n Enter the amount you want to withdraw from your account\t"))
            acc_check = banking_sys.get_account(acc_no)
            if acc_check:
                account = Account()
                account.get(acc_check, amount)
            else:
                print("\n Account not found.")
        elif option == 4:
            acc_no = input("\n Enter Account Number\t")
            acc_check = banking_sys.get_account(acc_no)
            if acc_check:
                print("\n Here's your account details\t ", acc_check)
            else:
                print("\n Account not found.")
        elif option == 5:
            del banking_sys
            exit()


if __name__ == "__main__":
    main()
