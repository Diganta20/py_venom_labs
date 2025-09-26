'''Abstract class refers to showing only the esential features of the object while hiding the rest'''
'''To achieve abstraction, we use the abc (Abstract Base Class) module'''
'''To apply abstraction : from abc implement ABC, abstractmethod
and pass ABC as argument to the class(ABC): this class will become abstract base class and the object of the abstract base class
cannot be initiated directly'''
'''We have to call @abstractmethod decorater inside abstract base class'''




from abc import ABC, abstractmethod

class Vehicle(ABC):  #this is the abstract class and its object cannot be initiated directly
    @abstractmethod                     #it has two abstract functions
    def start(): 
        pass  # in abstract class its best practice to not to declare body of a function and use pass key word instead
        

    @abstractmethod
    def stop():
        pass


class Car(Vehicle):
    def start(self):
        print("Car started usig key fob")

    def stop(self):
        print ("Car stopped using break")

class Bike(Vehicle):
    def start(self):
        print("Bike started with self")
    def stop(self):
        print("Bike stopped with disc brakes")

# v1=Vehicle()   Can't instantiate abstract class Vehicle
# v1.start()

c=Car()
b=Bike()

for x in (c,b):
    x.start()
    x.stop()