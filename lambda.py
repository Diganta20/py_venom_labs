'''lamba are short anonymys inline functions that are used any where in the code,
 ulike regular function you dont have to create the entire def bloack '''

#syntax;-  your_function_name = lambda inputs : output


#normal fuction

def add(a,b):
    return a+b
c=add(5,7)
d=add(10,5)
print(c,d)


#using lambda dunction

add=lambda x,y: x+y
print(add(5,5))

# or 

x=10
y=5
add=lambda x,y: x+y
z=add(x,y)
print(z)

#mult

mul=lambda l,m,n: l*m*n
print(mul(5,10,20))

'''lambda function can be used inside another function'''

#example

def func(n):
    return lambda x: x*n
mul=func(10)
print(mul(5))


#use function to make a function that always triples the number you send in:

def func1(n):
    return lambda x: x*n
triples=func1(3)
print(triples(10))

# Write a program using lambda functions to check 
# if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.

l = [2,4,7,3,14,19]
for i in l:
    odd=lambda i: i%2==0
    if i%2==0:
        print("false num is not odd",i)
    else:
        print('true the no is odd',i)
    

# though the ans is corect the approach is wrong also we have to check the condition and not hardcode

l = [2,4,7,3,14,19]
for i in l:
    lam=lambda i: (i%2)==1
    print(lam(i))


'''Imagine you run a coffee shop. Write a lambda function to calculate the bill after adding 18% GST to the base price.

Example: Input → 200, Output → 236.'''


aftertax= lambda c: (c*(.18))+c
print(aftertax(200))

'''You have a list of names: ["Ravi", "Anita", "Rahul", "Sneha"].
How would you use a lambda with sorted() to sort them by the last letter of each name'''

names = ["Ravi", "Anita", "Rahul", "Sneha"]

# sort by last letter
sorted_names = sorted(names, key=lambda name: name[-1])

print(sorted_names)