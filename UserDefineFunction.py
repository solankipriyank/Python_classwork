#function with no argument & no return value

def printline():
    print("*"*60)

printline()
print("welcome to user defined function in python.")

#function with argument & no return value

def sum(a,b):
    print("sum :",a+b)

printline()
x=int(input("Enter value :"))
y=int(input("Enter value :"))
sum(x,y)
printline()


#function with argument & return value

#def sub(a,b):
 #   print("sub :",a-b)
def sub(a,b):
    return a-b
printline()
x=int(input("Enter value :"))
y=int(input("Enter value :"))
ans=sub(x,y)
print("substrsction :",sub(x,y))
printline()
