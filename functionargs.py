

#normal function 

# def greet(name,message):                                
#     print(f"Hello,{name} {message}")

# name="Dev"
# message="Welcome to py"
# greet(name,message)

# x="Boss"
# y="We were waiting for your command"
# greet(x,y)

# z=7
# k=9
# greet(k,z)

'''What we can conclude from this is when we want to call the function the name of the function must be same
but its not necessary that name of arg be same as you can see we have passed x y k z'''


# function with unknown no of parameters is called arbitary arguments

'''Aribtary argument(*args), when you dont know the no of arguments to passed into the func,
then *args or add a * before keyword is passed into the function as argument, this will pass a tuple into the function'''

#exmaple 1 (easy)

def vehicle(*car):
    print("That's my car "  +  car[2])


car=("BMW","Merc","RR","Lambo")

vehicle(*car)








# def pasta(*ingredients):
#     print("This are the ingredients required to make a pasta ")
#     count=0
#     for i in ingredients:
#         count+=1
#         print(count,i)



# ingredients="pasta" ,"cheese", "milk"

# pasta(*ingredients)























