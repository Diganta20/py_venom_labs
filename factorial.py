'''factorial of num n= n*(n-1)(n-2)(n-3)....'''

# factorial using recursion
def func(n):
    if n==0:
        return 1
    else:
       return n* func(n-1)
    
factorial=func(5)
print(factorial)


#factorial using loop

def fun(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result

fact=fun(6)
print(fact)

