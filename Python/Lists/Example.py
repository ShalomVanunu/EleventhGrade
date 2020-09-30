


# declare
ii = []
my_list = [1,210,4,50,6,7,7,8] # declare list
print(len(my_list)) # how much values
print(my_list.index(7)) # bring the index of value
print(my_list.count(7)) # bring the mount of the value desire
print(" Reverse the List")
#print(reversed(my_list))
my_list.reverse()  # change the original List
print(my_list)
print(" Sorted the List")
print(sorted(my_list)) # dont change the original List
print(my_list)
print(" Sort the List")

my_list.sort() # change the original List
print(my_list)




print("________________________________________________________________")

my_list = [1,2,3,4,5,6,7] # declare list

for i in my_list:
    print(i)

print(my_list)
print(my_list[0:4]) # from index 0 to 3



print("________________________________________________________________")

my_list = []
my_list = [1,2,3,'example',3.123,'example']

del my_list[2] # remove with index
my_list.remove('example') # remove by value
my_list.pop(0) # remove with index
my_list.clear()
print(my_list)

print("________________________________________________________________")

my_list.extend([5,6,7,8]) # add more List
print(my_list)

print("________________________________________________________________")
my_list.append('number added') # add value to the end of the List
my_list.append(input("enter your name :"))
print(my_list)
print("________________________________________________________________")


my_list = [1,2,3,'example',3.123]

print(my_list)
print("________________________________________________________________")
