from random import randint

class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter your name =")
        # self.address = input("Enter your address = ")
        self.phone_number = int(input("Enter your Phone number = "))
        self.balance = 0

    def show_info(self):
        print(f"Account number = {self.account}")
        print(f"Full Name = {self.full_name}")
        print(f"Balance = {self.balance}\n")
    
    def show_balanced(self) -> None:
        print(f"Current balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient balanced : ")
        else:
            #self.balance -= amount
            self.balance = self.balance - amount
    
    def deposit(self) ->None:
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount

# b1 = Bank()
# b1.show_balanced()
# b1.withdraw()
# b1.show_balanced()
# b1.deposit()
# b1.show_balanced()
# Banks = []

# x = Bank()
# Banks.append(x)
# print(Banks)

# y = Bank()
# Banks.append(y)
# print(y)

# Banks[1].show_balanced()
# Banks[0].deposit()
# Banks[0].show_balanced()
Banks = []
while True:
    print("1 . Create account:")
    print("2. Show all bank details")
    print("3. Deposit amount")
    print("4.Exit")

    choice = int(input("Enter choice = "))

    if choice == 1 :
        obj = Bank()
        Banks.append(obj)
        print(Banks)

    elif choice == 2:
        if len(Banks) == 0:
            print("No account have been created yet")
        else:
            for account in Banks:
                account.show_info()

    elif choice == 3:
        if len(Banks) == 0:
            print("No account have been created yet..")
        else:
            acc_no = int(input("Enter account number to deposit = "))
            for obj in Banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break


    elif choice == 4:
        break
        

    else:
        print("Invalid Choice :")