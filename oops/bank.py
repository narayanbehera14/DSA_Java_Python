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
            print("Withdrawal sucessful")
    
    def deposit(self) ->None:
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount
        print("Deposit successfull..!")

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

def check_account_exists(acc_no: int):
    global Banks
    for obj in Banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("1. Create account:")
    print("2. Show all bank details")
    print("3. Deposit amount")
    print("4. withdraw amount")
    print("5. Transfer amount")
    print("6. Exit")

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
            found = False


            for obj in Banks:
                if obj.account == acc_no:
                    obj.deposit()
                    found = True
                    break
            
            if not found:
                print("Account does not exist")

    elif choice == 4:
        if len(Banks) == 0:
            print("No account have been created yet..")
        else:
            acc_no = int(input("Enter account number to withdraw = "))
            found = False

            for obj in Banks:
                if obj.account == acc_no:
                        
                        obj.withdraw()
                        found = True
                        break

            if not found:

                print("Account does not exist")


    elif choice == 5:
        from_acc_no = int(input("Enter account number from which you want to transfer = "))
        to_acc_no = int(input("Enter account number to which you want to transfer = "))
        from_acc_obj = check_account_exists(from_acc_no)
        to_acc_obj  = check_account_exists(to_acc_no)

        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter transfer amount = "))
            if from_acc_obj.balance < transfer_amount:
                print("Insuffcient balance")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount


        else:
            print("Account does not exists")

    elif choice == 6:
        break

    else:
        print("Invalid Choice :")