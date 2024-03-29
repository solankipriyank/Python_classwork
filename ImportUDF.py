import UDF

while True:
    print("*"*50)
    print("1.OddEven")
    print("2.Max of Two")
    print("3.Max of Three")
    print("4.Prime")
    print("5.Fibonacci")
    print("6.Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice :"))
    print("*"*50)

    if choice==1:
        a=int(input("Enter Value :"))
        UDF.oddeven(a)
        print("*"*50)
    elif choice==2:
        a=int(input("Enter Value :"))
        b=int(input("Enter Value :"))
        UDF.maxoftwo(a,b)
        print("*"*50)
    elif choice==3:
        a=int(input("Enter Value :"))
        b=int(input("Enter Value :"))
        c=int(input("Enter Value :"))
        UDF.maxofthree(a,b,c)
        print("*"*50)
    elif choice==4:
        a=int(input("Enter Value :"))
        UDF.prime(a)
        print("*"*50)
    elif choice==5:
        a=int(input("Enter Value :"))
        UDF.fibonacci(a)
        print("*"*50)
    elif choice==6:
        print("Thank You For Using Our Service.")
        print("*"*50)
        break
    else:
        print("Invalid Choice .Please Try Again.")
        print("*"*50)
