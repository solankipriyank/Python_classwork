file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File written successfully")
print("*****************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*****************")

file=open("tops1.txt","a")
file.write("\n This file is now appended.")
file.close()
print("File Appended Successfully")
print("*****************")

file=open("tops1.txt","r")
print(file.read())
file.close()

file=open("tops2.txt","w+")
file.write("This is w+ Mode using python.")
print("file current positon :",file.tell())
file.seek(0)
print(file.read())
file.close()
print("************")
