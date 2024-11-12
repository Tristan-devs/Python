# Python day 1 - am

# Run file either by hitting play button top right, or by right clicking the file, and choosing 'run python in terminal'

# unicode 
# We write in snake case in python 
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

print(f"{format_output}---START---{format_reset}")

# Print outputs to terminal, like console.log in javascript
print("Hello World")

print(2+2)

# We use comma to seperate variables in a print statement 
print("Current day of month:", 4)

# What if we want quote marks inside our string

print('My name is "Tristan"')

print("My name is \"Tristan\"")

# Variables 
# We dont need to use any declerations to declare a vaiable

greeting = "Good Day"

print(greeting)

# Reassigning the value of our vaiable 
# Does not change previous print statement 

greeting = "Good Night"

print(greeting)

# In python constants are declared by a practice and are not a seperate type of variable 
# We indicate what should be constant by declaring it in capital letters 

NAME = "Tristan"

print(NAME)

# However it can still be reassigned 
# DO NOT DO THIS 

NAME = "Elliot"

print(NAME)

# Data Types

# String is a text data type
string = "Character between quote marks"

# Boolean is wither true or false first letter is capitalised
boolean = True

# Integer is a whole number
integer = 5

# Float is a deciaml number 
#float = 2.3

# We can find the data type of a vaiable 

print(type(string))
print(type(boolean))
print(type(integer))
print(type(float))

# an F string is like a template literal in javascript 
# We can use it to pass variables into our strings 
# We place an 'f' before the string, and {} around the variable name

day = "Monday"
print(f"Today is {day}")

print("------------------------------------------------------------------------")
# Create a variable "name" and assign a string containing your first name as its value, then print the variable to the console.
NAME = "Tristan"
print(NAME)
# Update the value of your "name" variable to contain your full name. 
NAME = "Tristan Stanton"

print(NAME)
# Create 2 more variables named "age" and "city" and assign them your age as a number and your city of residence as a string. 
age = 21

city = "Gateshead"
# Finally, print an f{string} to the console of a sentence containing the name, age and city information. eg: "My name is Dave, I'm 25 and live in London"

print(f"My name is {NAME}, Iam {age} and I live in {city}.")

user_name = input("Please enter your name: ")
print(f"Hello, {user_name}!")

user_age = input("How old are you: ")

user_city = input("What city are you from: ")

print(f"My name is {user_name}, Iam {user_age} and I live in {user_city}.")

# Use input to obtain 2 numbers from a user, once obtained add the 2 numbers provided together and print the result to the console.

num1 = input("Give me any number: ")
num2 = input ("Give me any number: ")

num1 = float(num1)
num2 = float(num2)

result = num1 + num2

print(f"The sum of {num1} and {num2} is {result}")

# conditional example 

num = 1111

if num > 1000:
    print("Greater than 1000")
elif num > 100: 
    print("Greater than 100")
else:
    print("100 or less")

#math statement / match case 
# equivalent to a switch case in javascript 

day = "Monday"

match day:
    case "Monday":
        print("oh lord no")
    case "Friday":
        print ("Almost there")
    case "Saturday":
        print ("It is the weekend")
    case _: # default. anything else
        print ("Boring weekday")


#mathmatical operators

x = 5 + 5

print(x)

y = 7 - 3

print (y)

z = 3 * 5 

print (z)

p = int (10 / 2) # division defaults to float. here we have type cast p to be an integer 
print (p) # floats converted into integers simply remove everything after the decimal point

#modulus
r = 5 % 2 
print (r)

# logical operators 

# Equal
#python is more strict on data types than javascript
# this means that there is no === un python as all comparisons check for data types
o = 12
# if o's value is '12' this will no longer be equal
if o == 12:
    print("Equal")
else:
    print("Not equal")

# < & >
if o < 20:
    print("Less than 20")

# <= & >=
if o <= 12:
    print("Less than or equal to 12")

# not equal to 
if o != 2141432:
    print ("Shockingly, not equal to 2141432")

#logical operators 

t = 121

if t > 100 and t < 1000:
    print ("Between 100 & 1000")

if t == 100 or t == 50:
    print("T is either 100 or 50")


# Get the test score from the user
score = int(input("Enter the student's test score (0-100): "))

# Determine the grade
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score"

# Print the result
print(f"The student's grade is: {grade}")

# Get a number from the user
number = float(input("Enter a number: "))

# Check the number using nested if statements
if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")


