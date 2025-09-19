# count = 1
# while count <= 5:      #while loop syntax
#     print(count)
#     count += 1 

attempts=0
enter_password=""
while enter_password!="hellopy":
    enter_password=input("Enter password:")
    if attempts>=5:
     print("Too many attempts, password is locked")
    attempts+=1

print(f"Your password is {enter_password}. It took you {attempts} attempts.")


