
student_name = input("Enter student name: ")
ts = int(input("Enter theory test score (0-100): "))
    
if ts <= 40:
    print("failed in theory sub")
    exit()
    
ps = int(input("Enter practical test score (0-100): "))
if ps <= 40:
    print("failed in practical sub")
    exit()

x=(ts+ps)/2
print(x)

if x>=95:
    print("Grade : A")
elif x<=94 and x>=90:
    print("Grade : B")
elif x<=89 and x>=60:
    print("Grade : c")
elif x<=59 and x>=40:
    print("Grade : d")
else:
    print("Fail")

 #now if we want to end the code if ps or ts is >40 then we can use return or exit()
 
