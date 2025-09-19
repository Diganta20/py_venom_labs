m=int(input("Enter marks:"))
match m:
    case _ if m in range (90,101):
        print("Grade: A")
    case _ if m in range (80,90):
        print("Grade: B")
    case _ if m in range (70,80):
        print("Grade: C")
    case _ if m in range (60,70):
        print("Grade: D")
    case _ if m in range (0,60):
        print("Grade: Failed")
    