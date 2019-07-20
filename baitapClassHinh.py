lass Hinh:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "hình "+ self.name
     


class HinhTron(Hinh):
    def __init__(self,r):
        self.name="tròn"
        self.r=r
        self.pi=3.14
    def dientich(self):
        s=self.pi*self.r*self.r
        print(s)
        return(s)
    def chuvi(self):
        p=2*self.pi*self.r
        print(p)
        return p

class Hinhvuong(Hinh):
    def __init__(self,a):
        self.name="vuông"
        self.a=a

    def dientich(self):
        s=self.a*self.a
        print(s)
        return s
    def chuvi(self):
        p=self.a*4
        print(p)
        return p
import math    
class HinhTamGiac(Hinh):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def chuvi(self):
        p=self.a+self.b+self.c
        print(p)
        return p
    def dientich(self):
        p=self.chuvi()/2
        s=math.sqrt(p*(p-self.a)(p-self.b)(p-self.c))
        print(s)
        return(s)
        
