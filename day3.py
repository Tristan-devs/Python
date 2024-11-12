format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

print(f"{format_output}---START---{format_reset}")

# TUPLES
# Tuples are immutable data collections
# think of them as lists that dont change 

fruits = ("apple", "orange", "banana")

# we can print out the whole tuple or individual entries in the same way as we do with a list
print(fruits)
print(fruits[1])

# this is not allowed with a tuple 
#fruits[1] = "mango"
#print(fruits)

print("Items in Tuple:", len(fruits))

for fruit in fruits:
    print(fruit)

# Tuple are most useful for read only data 
# they can also be stored in sets & dictionareies 

# SETS

#Sets are unordered collection of unique data points 

days_of_week = {"Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
print(days_of_week)

# Sets will not include duplicate values, like the 'monday' below
days_of_week = {"Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"}
print(days_of_week)

weekend = {"Saturday", "Sunday"}

print(days_of_week.intersection(weekend))

# this can also be written with &
print(days_of_week & weekend)

# difference allows us to access values that are in the first set, but not the second 
print(days_of_week.difference(weekend))

print(weekend.difference(days_of_week))

# this can also be written wit a minus ' - '
print(days_of_week - weekend)

# Union 
weekdays = {"Monday", "Tuesday","Wednesday","Thursday","Friday"}

full_week = weekdays.union(weekend)
print(full_week)

# can also be written using |
week = weekdays | weekend
print(week)
