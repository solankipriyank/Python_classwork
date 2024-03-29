print("strat code")
try:
    a=int(input("Enter A :"))
    b=int(input("Enter B :"))
    c=a/b
    print("Division :",c)
    l=[1,2,3,4,5]
    index=int(input("Enter index number :"))
    print("Data at index",index,"is :",l[index])
except ZeroDivisionError as e:    #except exception as e:
    print("Exception caught :",e)  #print("Exception caught :",e)
except ValueError as e:
    print("Exception caught :",e)
except IndexError as e:
    print("Exception caught :",e)
finally:
    print("Finally Block")
print("End code ")

