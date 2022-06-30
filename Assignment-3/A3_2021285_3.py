from datetime import datetime

class BankAccount:
    def __init__(self,username,password,current_balance):
        self.user=username
        self.p=password
        self.cb=current_balance

        with open(f'{username}.txt','w') as f:
            f.write(f"This is {username}'s Transaction History\n")

    def Authenticate(self):
        pwd=input("PLEASE ENTER YOUR SECRET PASSWORD: ")
        if pwd==self.p:
            return True
        else:
            return False

    def Deposit(self,dep_amt):
        n=1
        try:
            while True:
                assert n<3
                flag=BankAccount.Authenticate(self)
                if flag==True:
                    break
                else:
                    print("PLEASE RE-ENTER PASSWORD!!")
        except:
            print("TOO MANY WRONG ATTEMPTS!!. OPERATION NOT EXECUTED. TRY AGAIN.")

        if flag==True:
            self.cb+=dep_amt
            with open(f'{self.user}.txt','a') as f:
                f.write(f"{datetime.now()}   The amount of Rupees {dep_amt} has been added   Current Balance --> {self.cb}\n")
            
        
    def Withdraw(self,deb_amt):
        n=1
        try:
            while True:
                assert n<3
                flag=BankAccount.Authenticate(self)
                if flag==True:
                    break
                else:
                    print("PLEASE RE-ENTER PASSWORD!!")
        except:
            print("TOO MANY WRONG ATTEMPTS!!. OPERATION NOT EXECUTED. TRY AGAIN")

        try:
            assert deb_amt<self.cb
            if flag==True:
                self.cb-=deb_amt
                with open(f"{self.user}.txt",'a') as f:
                    f.write(f"{datetime.now()}   The amount of Rupees {deb_amt} has been debited   Current Balance--> {self.cb}\n")
        except:
            print("LOW BALANCE! CANNOT BE DEBITTED AT THIS MOMENT!")

    def BankStatement(self):
        n=1
        try:
            while True:
                assert n<3
                flag=BankAccount.Authenticate(self)
                if flag==True:
                    break
                else:
                    print("PLEASE RE-ENTER PASSWORD!!")
        except:
            print("TOO MANY WRONG ATTEMPTS!!. OPERATION NOT EXECUTED. TRY AGAIN")

        if flag==True:
            with open(f'{self.user}.txt','r') as f:
                for i in f:
                    l=[j.strip() for j in f]
                    for i in l:
                        print(i)

# THE MAIN CODE STARTS HERE

print("WELCOME TO BANK OF IIITD")
l_menu=['Deposit a sum into account','Withdraw a sum from account','View Transaction History','Quit']


# Asking the user for initial inputs

username=input("ENTER YOUR USERNAME: ")
while True:
    try:
        password=input("ENTER ONLY 5 DIGITS PASSWORD: ")
        assert len(password)==5
        break
    except:
        print("INVALID ENTER 5 DIGIT PASSWORD")

current_balance=int(input("ENTER YOUR CURRENT BALANCE: "))

# Executing the menu based operations in program

customer1=BankAccount(username,password,current_balance)
flag_continue=1

while flag_continue==1:

    for i,j in enumerate(l_menu):
        print(f"{i+1} {j}")
    try:
        op=int(input("CHOOSE THE NUMBER AGAINST THE OPERATION YOU WISH TO EXECUTE: "))
        assert op>0 and op<5
    except:
        print("INVALID ENTRY")


    if op==1: # DEPOSIT SUM INTO YOUR ACCOUNT
        dep_amt=int(input("ENTER THE AMOUNT YOU WISH TO DEPOSIT: "))
        customer1.Deposit(dep_amt)
        continue

    if op==2: # WITHDRAW SUM FROM YOUR ACCOUNT
        deb_amt=int(input("ENTER THE AMOUNT YOU WISH TO WITHDRAW FROM YOUR ACCOUNT: "))
        customer1.Withdraw(deb_amt)
        continue

    if op==3: # VIEW TRANSACTION HISTORY
        customer1.BankStatement()
        continue

    if op==4:
        flag_continue=0
        continue











