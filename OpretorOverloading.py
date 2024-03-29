class Point:
    def __init__(self,x,y):
        print("init Called")
        self.x=x
        self.y=y
    def __str__(self):
        print("Str Called")
        return "[{0},{1}]".format(self.x,self.y)
    def __add__(self,obj):
        print("Add Called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)
p1=Point(50,50)
print(p1)
p2=Point(50,50)
print(p2)
print("Addition Of 2 Objects : ",p1+p2)
