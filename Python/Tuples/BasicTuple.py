


"""
Example
"""

data = (1,3,5,"bye", 5.5)

print(data)

print(data[3]) # bye
print(data[1:3]) # 3,5
print(data[::2]) # only even

print("________________________________________________________________")
# insert argument
#data[0] =10 # Error . in Tuple you cant change values!!

# change value on Tuple
my_new_data = list(data)
print(my_new_data)
my_new_data[0] = 10 # insert value
data = tuple(my_new_data)
print(data)

print("________________________________________________________________")

data1 = (3,)
print(type(data1))

