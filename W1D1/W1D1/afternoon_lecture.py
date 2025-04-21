"""
In JavaScript (For loop)
for(var count=0; count<10; count++){
    console.log(count);
}
"""
# Python
"""
range = function that returns a sequence of numbers
start: has a default value of 0 (optional)
stop: required
step: (optional) with a default value 1
"""
# for count in range(10):
#     print(count)
# for count in range(1,10,2):
#     print(count)
# for c in range(10,0,-1):
#     print(c)

# for i in range(0,10,2):
#     print(f"i= {i}")
#     for j in range(0, i):
#         print(f"j= {j}")

super_heros = ["Batman", "Superman", "Aquaman", "Spiderman", "Wonderwoman"]
        
"""
In JavaScript (For loop)
for(var count=0; count<super_heros.length; count++){
    console.log(super_heros[count]);
}
"""

# Python
# for index in range(len(super_heros)):
#     print(super_heros[index])
# print("*"*100)
# for hero in super_heros:
#     print(hero)
    
# my_list=["Hello", "Dojo", [None, 4, 5, 6],1,2,3, {"name": "Mohamed", "email": "m@m.m"}]
# for item in my_list:
#     print(item)
#     for i in item:
#         print(i)

user={
    "first_name": "Mehrez",
    "last_name": "riadh",
    "age": 31,
    "is_player": True,
    "hobbies": ["control", "video games", "parties"],
    "friends": {"one":"Mustapha", "two": "Rayen", "three": "Kossay", "four":"Raed"}
}
# for k, v in user.items():
#     print(f"{k}: {v}")
    
# for key in user.keys():
#     print(key)
# for value in user.values():
#     print(value)

# x = 5
# while x>0:
#     print(x)
#     x-=1
    
# Functions
""" 
In JavaScript
function functionName(agrs){
    instructions
}
"""

""" 
function ? => set of instructions to not repeat same code
optional agrs
return statement is Must!!!!!!!
"""
# def say_hi():
#     print("Hello")
#     return "Hello"
# result=say_hi()
# print(result)

# def sum_numbers(a, b):
#     return a+b
# print(sum_numbers(2,6))

def sum_numbers(*params):
    sum = 0
    for p in params:
        sum += p
    return sum
        
    
# print(sum_numbers(1,2,3,4)) # params = [1,2,3,4]
# print(sum_numbers(1,2,3,4,5,6,7,8,9)) # params = [1,2,3,4,5,6,7,8,9]
# print(sum_numbers()) # params = []

def say_hi_fullname(**kvargs):
    print(kvargs)
    return None

say_hi_fullname(first_name="Joe", last_name= "Doe")
say_hi_fullname(first_name="Joe", last_name= "Doe", age=20, is_admin=True)