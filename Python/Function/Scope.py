"""
Scope program
"""

number_one = 10


def print_number():
    number_two = 5
    print(number_one+number_two)



print_number()

print("________________________________________________________________")
number = 10
NUMBER_OF_STUDENTS = 40

def print_number():
    global number
    number = 5
    print(NUMBER_OF_STUDENTS)



print_number()
print(number)

print("________________________________________________________________")
number = 10

def print_number():
    number = 5
    print(number)


print(number)
print_number()

print("________________________________________________________________")
#Global argument
number = 10

def print_number():
    print(number)


print(number)
print_number()
