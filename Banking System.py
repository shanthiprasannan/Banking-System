import random
import sys
from AccDetails import Account

class Bank:
    def __init__(self):
        print("Welcome to the Banking System\n")
        m=int(input("1 : For Banking Transaction\n2 : New User "))
        if m==1:
            a=input("Enter your user name: ")
            b=input("enter your password : ")
            self.user=a
            self.pw=b
            self.login()
        elif m==2:
            self.new_account()
        else:
            print("please enter a valid number\n")
            self.__init__()
    def login(self):
        if self.user in Account and self.pw in Account[self.user]["pw"]:
             print("1 : Withdrawal\n 2 : Deposit \n 3 : To check the balance \n 4 : Cancel the Transaction")
             num1=int(input("enter your option\n"))
             if num1==1:
                self.withdrawal()
             elif num1==2:
                self.deposit()
             elif num1==3:
                self.balance()
             elif num1==4:
                sys.exit()

             else:
                print("Invalid number")
                self.login()
        else:
            print("Invalid user name or password\n")
            x=int(input("If you want to continue the transaction please enter 1 \n To Exit please enter 2 "))
            if x==1:
               self.__init__()
            else:
                sys.exit()

    def balance(self):
        print("your current balance is : ",Account[self.user]["balance"])
        sys.exit()



    def deposit(self):
        cd=int(input("Enter the amount to be deposited : "))
        with open("AccDetails.py","r") as file:
            content =file.read()
            content = content.replace(f"{Account[self.user]['balance']}",f"{Account[self.user]['balance']+cd}")
        with open("AccDetails.py","w") as file:
            file.write(content)
        print(f"Rs {cd} successfully credited to your account.\n Current Balance : ", Account[self.user]['balance']+cd)
        print("\n")
        self.login()


    def withdrawal(self):
        cw =int(input("Enter the amount to be depited : "))
        if cw<=Account[self.user]['balance']:
            with open("AccDetails.py","r") as file:
                content =file.read()
                content = content.replace(f"{Account[self.user]['balance']}",f"{Account[self.user]['balance']-cw}")
            with open("AccDetails.py","w") as file:
                 file.write(content)
            print(f"Rs {cw} debited from your account.\n Current Balance : ", Account[self.user]['balance']-cw)

        else:
            print("Insufficient fund \n")
            self.login()

    def new_account(self):
        name = input("Enter your name: ")
        e_mail = input("Enter your e-mail id: ")
        phone_no = int(input("Enter your phone: "))
        acc_no = random.randint(1010, 9999)
        balance = 0
        print(f"Your account number is {acc_no}")
        print("Create an username and password for your account")
        user1 = input("Create an username: ")
        pass_word = input("Create a new password: ")
        if user1 not in Account:
            Account[user1] = {'acno': acc_no, 'name': name,'pw': pass_word, 'balance': balance,
                              'phno': phone_no,'email': e_mail}
            print("You have successfully created your account\n ")
            print("Login again for accessing your account")
            with open("AccDetails.py", "w") as file:
                file.write(f"Account = {Account} \n")
            self.__init__()
        else:
            print("username Already exist")

            self.new_account()




B1= Bank()
B1.__init__()









