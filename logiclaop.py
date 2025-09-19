#or



#and 
a=500
b=400
print(a==b and a>b)
# and gives o/p True only if both the conditions are ture
a=500
b=400
print(b<a and a>b)

# or
a=500
b=400
print("or is",b==a or a>b)
# or gives o/p True if any of the conditions are true
a=500
b=900
print(b<a or a>b)
# not
a=500
b=400
print (not(b<a and a>b))
a=500
b=400
print (not(b==a or a<b))
# not gives the revered o/p of any o/p eg. if the op is T then not gives op false 

print(5/3) #normal divison
print(5//3) #this is floor divison it returns the nearest whole no
print(-5//3) #in case of a -ve the floor divison returns the whole no closest to -ve side
print(5%3) #this is modulus operator it returns the remainder of the divison