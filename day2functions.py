format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

print(f"{format_output}---START---{format_reset}")

# FUNCTIONS 

# here we're declaring a simple function in a similar way to how we did in javascript
def greeting():
    print("Hello world")

greeting()

# and here we are passing in name as an argument, refer to a spcific user 
username = "Tristan"

def greet_by_name(name):
    print(f"Hello {name}!")

greet_by_name(username)

# default arguments 

def greet_user(message = "Hello" , name = "you"):
    print(f"{message} {name}!")

greet_user()

# addition function
# returns allows us to create functions that output useful information & data, to be used elsewhere
def add (a,b):
    return a + b

x = add(3,2)

print(x)

# using a return allows us to use our function as an parameters 
y = add(add(7,15.5),add(16,82))
print(y)

# *arguments allows us to pass in an undifined amount of arguments 

def add_numbers(*nums):
    print(sum(nums))

# this takes in 4 numbers, even though we only defined one parameter, thanks to the * 

add_numbers(1,2,3,4)

print(f"{format_output}---START---{format_reset}")

# MODULES

# python has prebuilt modules that many developers will use 
import random

# random module allows us to grab random numbers, among other things 
x = random.randint(3,9)
print(x)

import calculator
print(calculator.calc_add(3,7))

# A function that uses input to obtain a user's name and returns a string greeting them by their name.
yourname = input("Hello what is you name?")

def greet_by_name(name):
    print(f"Hello {name}!")

greet_by_name(yourname)

# A function with parameters of 'name' and 'age' that returns a string containing the 'name' and 'age' supplied to it as arguments. Set a default argument of 'unknown' for 'age'.

def introduce(name, age='unknown'):
    return f"My name is {name} and I am {age} years old."


print(introduce("Alice"))        
print(introduce("Bob", 30))      

# A function that uses input to obtain a users name and age and checks whether or not the user is over the age of 18. # 
# If the user is over the age of 18, return a string containing their name advising that their sign-up has been successful. # 
# If a user is under the age of 18, return a string containing their name and age advising that they are unable to register due to their age.


print(50 * "=")

def check_signup():
    # Get the user's name
    name = input("Enter your name: ")
    
    # Get the user's age
    age = int(input("Enter your age: "))
    
    # Check if the user is over 18
    if age > 18:
        return f"Hello {name}, your sign-up has been successful!"
    else:
        return f"Sorry {name}, you are {age} years old and unable to register due to your age."

# Example usage
result = check_signup()
print(result)
