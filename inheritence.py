# '''Inheritence defines a class that inherits all its properties and method from another class.
# The class from which the properties or methods are inherited is called parent class aka base class.
# The class inherits from another class is called child class aka devired class .'''

# '''To inherit from parent class, the parent class is passed as an argument while creating the child class,
# in other words in order to create a child class pass the parent as an argument to the child class'''

# '''Suppose class Animal(): is the parent class, the child class dog would be-- class Dog(Animal):  '''

# '''Example 1'''

# # class Animal():    #parent class
# #     def __init__(self,name,diet):
# #         self.name=name
# #         self.diet=diet
# #     def info(self):
# #         return (f"name of the animal {self.name} and fav food is {self.diet}" )

# # cat1=Animal("Billy","Fish")  #object of parent class not necessary for child class this is here just for understanding
# # cat2=Animal("Miley Cirus","Milk")
# # i=cat1.info()
# # j=cat2.info()
# # print(i)
# # print(j)


# # class Dog(Animal):   #child class
# #     def sound(self):
# #         print(f"{self.name} barks")

# # d=Dog("Ghontu","Chicken")
# # d.sound()
# # k=d.info()   #inherited from parent class 
# # print(k)


# '''Example 2'''
# '''Adding __init__ method to child class, this will over ride the parents class __init__  method '''


# class Animal():
#     def __init__(self,name,diet):
#         self.name=name
#         self.diet=diet
#     def info(self):
#         print(f"Hello I am {self.name}, and my fav food is {self.diet}")
    
# class Dog(Animal):
#     def __init__(self,name, breed,diet):
#         super().__init__(name,diet)
#         self.breed=breed
#     def type_of_dog(self):
#         print(f"I am an {self.breed}")

# d=Dog("Ghontu","Indie","Chicken")
# d2=Dog("Bob","Indie","Mutton")
# d.info()                    #''' this throws an error as __init__ is overriden to fix this super() keyword is used '''
# d.type_of_dog()
# d2.info()
# d2.type_of_dog()

# #example 3
# class car():                                   
#     def __init__(self,brand,model,year): 
#         self.brand=brand
#         self.model=model               
#         self.year=year                  
#     def start(self):  
#         print("car started") 
#     def info(self):
#         print(f"your car's details: brand={self.brand}, model={self.model}, year_of_make={self.year}")


# class Auto(car):
#     def __init__(self, brand, model, year,type):
#         super().__init__(brand, model, year)
#         self.type=type                  #only the newly created parameter of child class has to be declared here with self.
#     def type_of_car(self,gear):             #here self and gear both have to passed because if self is not passed and you pass 
#         print(f"it's a {self.type} of car and its {gear}")  # only gear it will produce an error saying  takes 1 positional argument but 2 were given
#     def rev(self,rpm):                                         #and this happens because self is automatically passed to any func within a class
#         print(f"Its revs at {rpm}")

# a1=Auto("honda","city","2024","sedan")
# a1.start()
# a1.info()
# a1.type_of_car("automatic")              
# a1.rev(3000)

'''You can see I have passed gear and rpm but have not initialsed them using self. and that's why I have to pass their argument while
calling the function in line 86,87 to over come that 3.1 '''

#example 3.1

class car():                                   
    def __init__(self,brand,model,year): 
        self.brand=brand
        self.model=model               
        self.year=year                  
    def start(self):  
        print("car started") 
    def info(self):
        print(f"your car's details: brand={self.brand}, model={self.model}, year_of_make={self.year}")


class Auto(car):
    def __init__(self, brand, model, year,type,gear,rpm):
        super().__init__(brand, model, year)
        self.type=type
        self.gear=gear
        self.rpm=rpm
    def type_of_car(self):             
        print(f"it's a {self.type} of car and its {self.gear}")  
    def rev(self):
                                             
        print(f"Its revs at {self.rpm}")

a2=Auto("Nissan","Gtr","1998","Muscle","Manual","9000")
a2.start()
a2.info()
a2.type_of_car()
a2.rev()






