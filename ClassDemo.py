class Student:
    def getData(self,fname,mname,lname):
        
        print("get data called")
        self.f=fname
        self.m=mname
        self.l=lname
    def putData(self):
        print("Put data called")
        print("first name :",self.f)
        print("middle name :",self.m)
        print("last name :",self.l)

s1=Student()
s1.getData("solanki","priyank","laljibhai")
s1.putData()
