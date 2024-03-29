class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello",self.cname,"Your Account Number ",str(self.acno),"Open with",str(self.balance))
    def deposite(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("insufficienr balance")
    def checkbalance(self):
        print("Current balance :",self.balance)

b1=Bank()
cname=input("Enter Customer Name :")
acno=int(input("Enter Account Number :"))
balance=input("Enter Initial Balance :")
b1.openAccount(cname,acno,balance)

while True:
    print("******************************")
    print("1.Deposite")
    print("2.Withdraw")
    print("3.CheckBalance")
    print("4.Exit")

    choice=int(input("Enter Your Choice :"))
    print("******************************")

    if choice==1:
        amount=int(input("Enter Deposite Amount :"))
        b1.deposite(amount)
        print("**************************")
    elif choice==2:
        amount=int(input("Enter Withdraw Amount :"))
        b1.withdraw(amount)
        print("**************************")
    elif choice==3:
        b1.checkbalance()
        print("**************************")
    elif choice==4:
        print("Thank you for using our services.")
        print("**************************")
    else:
        print("Invalid choice Plaese Try Again.")
