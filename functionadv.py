

#normal function 

def greet(name,message):                                
    print(f"Hello,{name} {message}")

name="Dev"
message="Welcome to py"
greet(name,message)

x="Boss"
y="We were waiting for your command"
greet(x,y)

z=7
k=9
greet(k,z)

'''What we can conclude from this is when we want to call the function the name of the function must be same
but its not necessary that name of arg be same as you can see we have passed x y k z'''


# function with unknown no of parameters is called arbitary arguments

'''Aribtary argument(*args), when you dont know the no of arguments to passed into the func,
then *args or add a * before argument is passed into the function as argument, this will pass a tuple into the function'''

#exmaple 1 (easy)

def vehicle(*car):
    print("That's my car "  +  car[2])


car=("BMW","Merc","RR","Lambo")

vehicle(*car)


#Example 2
def pasta(*ingredients):
    print("This are the ingredients required to make a pasta ")
    count=0
    for i in ingredients:
        count+=1
        print(count,i)



ingredients="pasta" ,"cheese", "milk"
print(type(ingredients))
pasta(*ingredients)



#example 3



# def cars(*speed):
#     print("These are some powerful cars:")
#     for i in speed:
#         print("#",i)


# a=input("Enter names of hyper-cars:")
# speed=a.split(",")
# print(type(speed))
# cars(*speed)



'''Keyword arguments: You can send arguments in key=value pair syntax, in this way the order of argument wont matter'''

def subs(sub1,sub2,sub3):
    print("this is my fav sub: "   +sub2)

subs(sub1="py",sub2="dsa",sub3='js')


'''**kwargs is used when you dont know the exact no of key=value arguments you have to pass'''
#example1 
def fun(**kids):
    print("Youngest kid is " +kids["kid2"])

fun(kid1="joy",kid2="Dev",kid3="Nak")


#example2


def func(**cars):
    count=0
    for key,value in cars.items():    #.item() is used to iterate over a loop and get key=value or key:value pair
        # if we want only the value then .value or for key .key
        
        print(count,"This car belongs to",key ,value )
        count+=1

func(car1="201",car2="205",car3="208")


#example3

def pasta(**ingredients):
    for key,value in ingredients.items():
        print("These are the required ingredients for pasta",key,value)



pasta(tomato="2",cheese="mozrella",typeofpasta="pene",milk=".5")


'''If we call the function without argument, it uses the default value!
we can pass an agrument with = in function'''


def func(country="India"):
    print(f"{country} is my country")

func(country="USA")
func(country="UK")
func(country="AUS")
func(country="DUBAI")
func()


'''Passing a list as an argument'''

def func(cars):
    for i in cars:
        print(i)

vehicle=["audi","lambo","merc","bmw","rr","landrover"]

func(vehicle)

#example2
def func(cars):
    for i in cars:
        print("-------------",i)

cars=["audi","lambo","merc","bmw","rr","landrover"]

func(cars)


'''Return: is like reading out the op loud, use return keyword when you want to return something'''

def func(x):
    return x+5

print(func(5))


'''The pass Statement
Function definitions cannot be empty, but if you for some reason have a function definition with no content,
 put in the pass statement to avoid getting an error.'''

def func():
    pass

print(func())

















