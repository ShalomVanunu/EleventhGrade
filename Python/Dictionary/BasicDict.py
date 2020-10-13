

user_data = {} # {} this is dictionary

user_data = {'first_name': 'shalom', 'last_name':"vanunu", "proffesional":"teacher"}

# {value1 : value2} || value1 - key value2 - value

print(user_data.keys())
print(user_data.values())

print(user_data["proffesional"]) # bring the value value

if 'last_name' in user_data.keys():
    print("the key last_name exsists ")
else:
    print("the key last_name  doesnt exsists ")

print("________________________________________________________________")

#update key
user_data["age"] = 35
print(user_data)

user_data.pop("age")
print(user_data)