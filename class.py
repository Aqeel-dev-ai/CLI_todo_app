class Bank:
    name = "MCB"
    def __init__(self,amnt):
        self.amnt = amnt
    def debit(self,deb):
        print(f"Debit Ammount...{deb}")
        self.amnt += deb
        print(f"Your new balance is {self.amnt}")
    
    def credit(self, cred):
        print(f"credit Ammount... {cred}")
        if self.amnt<=0:
              print("Sorry you cannot credit")
        else:
            self.amnt -= cred
            print(f"Your new balance is {self.amnt}")
obj = Bank(0.00)

print("Welcome to MCB....\n ")
while "true":
    n = int(input("\n\nTo check balance press 1\nTo debit ammount press 2\nTo credit ammount press 3\nEnter .. "))
    print("\n")

    if n == 1:
            print(f"Your available balance is ... {obj.amnt}")  
    elif n==2:
            deb = int(input("Enter Ammount ... "))
            obj.debit(deb)
            
    elif n==3:
            cred = int(input("Enter Ammount ... "))
            obj.credit(cred)
    else:
            print("Invalid Input\n Please choose 1/2/3")



