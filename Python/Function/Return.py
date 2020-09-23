"""
return program
"""

def user_detail(username,age):
    print(f"my username is {username} and my age is {age}")

user_detail("shalom", 22)

print("________________________________________________________________")
def add(a,b):
    print(a+b)
    return None

add(4,5)

print("________________________________________________________________")
# this function return by default one arguments
def add_numbers(number_one ,number_two=6):
    return number_one+number_two


print(add_numbers(100))

print("________________________________________________________________")
# this function return by put argument
def add_numbers(number_one=4,number_two=6):
    return number_one+number_two


print(add_numbers(100,100))

print("________________________________________________________________")
# this function return by default arguments
def add_numbers(number_one=4,number_two=6):
    return number_one+number_two


print(add_numbers())
