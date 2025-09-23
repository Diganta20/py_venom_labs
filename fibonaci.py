'''Fibonaci is a series of number where each no is a sum of preceding two numbers, the first two no is often 0 and 1 and the 
rest is a sum , eg 0,1,1,2,3,5,8......n'''

#formula 
'''F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2), for n >= 2'''

#using recursion

def func(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return func(n-1) + func (n-2)

fibonaci=func(7)
print(fibonaci)


#using loop

def fun(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


print(fun(5))