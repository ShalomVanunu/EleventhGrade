
# Tranfer from List to String
my_list = ['my','Name','is','Arthur']
print(my_list)
my_string = " ".join(my_list) # " " before join is the string to join
print(my_string)

# Tranfer from String to List
my_string = " my name is Arthur. im 35 years old. im living in Rishon Le Zion."
my_list = my_string.split(".")
print(my_list)

