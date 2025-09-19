
a=5
b=10 #Firstly we made two variables a & b assinged them with val
def calGmean(a,b):  #then we def a function using def keyword and giving it a name calGmean(), so here calGmean is the name of the function
   mean=(a*b)+(a+b) #a,b are parameters that go inside the function
   print(mean) #this can also be written as def calgem(a,b):
   #print("mean:",(a*b)+(a+b)) works same  

calGmean(a,b) #in ln 8 and ln 11, we are calling the function
c=5
d=20
calGmean(c,d)  
c=15
d=10
calGmean(a,d)  
