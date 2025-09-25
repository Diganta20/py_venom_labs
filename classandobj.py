'''class is like a blueprint of an object and object is the instance of the class'''
'''In other words class is like a blueprint of the house which contains all the specifications and methods to be followed in order to 
build the house and class is like the real world house made from the blueprint'''


class bike():
    def __init__(self,make,speed):
        self.make=make
        self.speed=speed
    def specs(self):
        print("your bike is a powerful machine")
        print("it runs in")
re=bike("honda",200)
re.specs()

#example 2


class complex():
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def print(self):
        print(str(self.real) +"+"+ str(self.imag) + "j")
    def add(self,c):
        self.real+=c.real
        self.imag+=c.imag
c1=complex(10,20)
c1.print()
c2=complex(30,50)
c2.print()
c1.add(c2)



#example 3

class car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def start(self):  
        print("car started") 
    def info(self):
        print(f"your car's details: brand={self.brand}, model={self.model}, year_of_make={self.year}")


auto1=car("bmw","m4comp",2005)
auto2=car("audi","rs6sportsback",2010)
auto1.start()
auto1.info()
auto2.start()
auto2.info()








