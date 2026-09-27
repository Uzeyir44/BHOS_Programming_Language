name = input("What is your name: ")
age = int(input("What is your age: "))
num = int(input("What is your favourite number: "))

print(f"Your age in 10 years: {age+10}")
print(f"The square of your favourite number: {num**2}")

if (num % 2 == 0):
    print("Your favourite number is even")
else:
    print("Your favourite number is odd")

print(f"Hi {name}! In 10 years you'll be {age+10}. Your favourite nuber squared is {num**2}, and it is {"even" if num % 2 == 0 else "odd"}")

"""
Python input() always returns string because it was designed this way.
Main reasons behind it is that in your input you can mean anything let it be number
or text, therefore it always returns you a raw text, so it is your responsibility to later
convert it to any data type that you need in your code.

Regarding the second question we need to covert it to int before doing math operations as it will return 
errors otherwise or not the result thta we were expecting
"""