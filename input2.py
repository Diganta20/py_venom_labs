age_input=input('enter your age:')
age=int(age_input)
print('Your age is',input)
if age <= 0:
    print('Pls enter correct age')
elif age <= 18:
    print("Your'e a minor")
elif age >= 18 and age <= 65:
    print("Your'e an adult")
elif age >= 65:
    print("Your'e a senior citizen")