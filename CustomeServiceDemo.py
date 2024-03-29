class CustomerService:
    def prepaid(self):
        print("Your Call Transfer To Prepiad Service.")
    def postpaid(self):
        print("Your Call Transfer To Postpiad Service.")
    def credit(self):
        print("Your Call Transfer To CreditCard Agent.")
    def debit(self):
        print("Your Call Transfer To DebitCard Agent.")
c1=CustomerService()
c1.prepaid()
choice=input("Enter Your Choice :")
if choice=="Prepaid":
         c1.prepaid()
elif choice=="Postpaid":
          c1.postpaid()
elif choice=="CreditCard":
          c1.credit()
elif choice=="Debitcard":
          c1.debit()

while True:
    print("*****************")
    print("1.prepaid")
    print("2.postpaid")
    print("3.Creditcard")
    print("4.Debitcard")
    print("5.Exit")

    choice=int(input("Enter Your Choice :"))


    if choice==1:
        print("Your Call Transfer To Prepiad Service.")
    elif choice==2:
        print("Your Call Transfer To Postpiad Service.")
    elif choice==3:
        print("Your Call Transfer To CreditCard Agent.")
    elif choice==4:
        print("Your Call Transfer To DebitCard Agent.")
    elif choice==5:
        print("Thank You For Using Our Service.")
        break
    else:
        print("Invalid Choice..")
