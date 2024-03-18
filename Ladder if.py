rno=int(input("Enter roll no:"))
sname=input("Enter student name :")
s1=int(input("Enter marks of subject 1:"))
s2=int(input("Enter marks of subject 2:"))
s3=int(input("Enter marks of subject 3:"))

total=s1+s2+s3
per=total/3

print("roll no:",rno)
print("student name:",sname)
print("total:",total)
print("percentage:",per)

if per>=70:
    print("distinction")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>=40:
    print("pass class")
else:
    print("fail")
