import time
x,y,z=time.strftime("%H:%M:%S").split(":")
x=int(x)
y=int(y)
z=int(z)
if x>=18 or x<5:
    print("Good night")
elif x>=5 and x<12:
    print("Good morning")
elif x>=12 and x<18:
    print("Good evening")
print("Hour",x)
print("Min",y)
print("Sec",z)
