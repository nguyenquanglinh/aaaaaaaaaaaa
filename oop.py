class people:
    def __init__(self,name,tuoi,dia_chi):
        self.__name=""
        self.tuoi=tuoi
        self.dia_chi=dia_chi
        self.__axx=""
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value=="cho":
            print("go go")
        else:print("meo meo")

x=None
print(type(x))


class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self,sound):
        print(sound)
class Dog(Animal):
    pass


dog=Dog("cho")
dog.name="cho"
print(dog.name)



