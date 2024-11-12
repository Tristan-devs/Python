format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

print(f"{format_output}---START---{format_reset}")

# Lists & loops 

# Creating list
languages = ["JavaScript", "CSS", "HTL", "Python", "SQL"]

# Outputting list to console
print(languages)

# Outputting the first item in our list 
print(languages[0])

print(languages[1])

# Accessing the item at the end of our list 
print(languages[-1])

print(languages[-2])

print(languages[2])

# Changing the value of a list item 
languages[2] = "HTML"

print(languages[2])

# Adding item to a list 
# Append adds an item to the end of the list
languages.append("C#")
print(languages[5])

# Insert adds it at a specified index
languages.insert(2, "C++")
print(languages)

languages.append("C++")
print(languages)

# Remove the first instance of specified value
#languages.remove("C++")
#print(languages)

del languages[-1]
print(languages)

# Amount of languages, using the len method
print(len(languages))

# LOOPS

print(f"{format_output}---START---{format_reset}")

# Both of these are functionally the same
for language in languages:
    print(language)

for i in languages:
    print(i)

# Splitting the letters on different lines
myName = "Tristan"

for letter in myName:
    print(letter)

# For loops using range 

for i in range(5):
    print(i)

# Prints 1 to 5
for i in range(5):
    print(i+1)

# While loops

print(50 * "=")

iterator = 1
while iterator <= 5:
    print(iterator)
    iterator += 1

print(iterator)

while True:
    user_input = input ("I will keep going until you tell me to stop:")

    if user_input.lower() == "stop":
        print(user_input)
        print("No problem")
        break # Exits the loop, regardless of condition

print(50 * "=")

for t in range(10):
    print(t+1)

print(50 * "=")

i = 1
while i <= 10:
    print(i)
    i += 1

print(50 * "=")

i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

print(50 * "=")

i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1







