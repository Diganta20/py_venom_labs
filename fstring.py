# Write a Python program that takes a user's name and age as input, then prints a message using an f-string that says:

# "Hello, [name]! Next year, you will be [age + 1] years old."

# name = "Alice"
# age = 25
# print(f"My name is {name} and I am {age} years old.")
# The f before the string signals: "Hey Python, this is a template with placeholders!"

# Inside the curly braces {}, you can put any valid Python expression (variables, calculations, function calls).

# Python replaces those braces with actual values at runtime.


name=input("Enter Your Name: ")
age=int(input("Enter your current age: "))
print(f"Hello, {name}!Next year, you will be {age + 1} years old")