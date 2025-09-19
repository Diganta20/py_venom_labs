a=input("Enter the name of the student:")
b=input("Enter grades:")
b=int(b)
def evaluate_student(a,b):
    if b>=90:
        print("Grade A")
    elif b>=80 and b<=89:
        print("Grade B")
    elif b>=70 and b<=79:
        print("Grade C")
    elif b>=60 and b<=69:
        print("Grade D")
    elif b<60:
        print("Grade F,the student has failed")
    return(a,b)

evaluate_student(a,b)