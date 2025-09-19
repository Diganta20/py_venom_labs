#identity operators

a= 5              
b=10
c=a
print(a is c)     #identity operator is returns true if the operands are identical else it returns false 
print(a is not b) #identity operator is not returns true if the operands are not identical else it returns false 
print(a is b)
print(a is not c)


#membership operators
# in  returns true if operand is present in seq
# not in retturn true if operand is not present in seq
li=[1,2,3,4,5,6,7,8,9,10]
z=input("Enter any number:")
z=int(z)
if z in li:
    print("number is present in list")
else:
    print("number is not present in list")