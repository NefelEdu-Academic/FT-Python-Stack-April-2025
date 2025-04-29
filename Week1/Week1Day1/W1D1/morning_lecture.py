# This is a one line comment
"""
This is 
multi-line 
comment
"""
# Varibale Declaration
# JavaScript                        Vs        Python
# var varibaleName = "John";                  varibale_name = "John"
#  camelCase                                  snake_case
# GLOBAL VARIBALES
GLOBAL_VARIABLE = "python"
PORT = 5000
APP_NAME = "WEB_APP"
# Data Types
# String
first_string = "hello world, I'm 20 years old"
# Numbers
    # Integers
age = 41
    # Floats
price = 4.5
# Boolean
test = True
is_admin = False

# NoneType
permit = None

print(first_string)
# Format Strings
print("hello world, I'm " + str(age) + " years old")
print("hello world, I'm {} years old {}".format(age, price))
print(f"hello world, I'm {age} years old {price}")

# Complex Data Types
# List
#             0           1        2       3      4   5  6
#             0 ........................................ len(sports) - 1
sports = ["Tennis", "Swimming", "Sky", "Football",1 ,2 , 3 ]
#           -7         -6        -5      -4     -3  -2  -1
print(sports)
print(len(sports))
sports.append(4)
print(sports)
sports.pop()
print(sports)
print(sports[1])
print(sports[-6])
numbers = [11, 2, 5, 3, 15, 0, 7]
numbers.sort(reverse=True)
print(numbers)

# Dictionaries
# key-value pairs
user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": age
}
print(user['last_name'],user['first_name'])

print(f"last name: {user['last_name']}, first name: {user['first_name']}")

user["first_name"] = "Jane"
print(user)

# Tuples
# similar to lists but immutable : can not be changed
hobbies = ("sport", "reading", "learning", "coding", "eating")
print(hobbies[3])
#! hobbies[2] = "traveling"
print(hobbies)

# Set
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,"Bob", "Bob", "Bob", "Alex", "Alex", True, True, True, False, False]
my_list2 = [15,1, 3, 2, 2, 30, 30, 30, 14, 14, 14, 14]
my_set = set(my_list2)
print(my_set)
# Condition: In JavaScript
# if(age < 9){
#console.log("Maybe next year")
# }else if(age >= 9 && age <= 15){
#     console.log("Welcome")
# }else{
#     console.log("Sorry you're too old")
# }
print(age)
# Python
if age < 9:
    print("Maybe next year")
elif age >= 9 and age <= 15:
    print("Welcome")
else:
    print("Sorry you're too old")