import string

user_input = input("Enter a Message :").replace(" ","").lower()
key = input("Enter the key :").lower()

input_list = list(user_input)
key_list = list(key)
letters = list(string.ascii_lowercase)

new_key_list = []
for x in range(len(input_list)): #אורך של המשפט
    new_key_list.append(key_list[x%len(key_list)])

print(input_list)
print(new_key_list)

sentence = []
for letter in input_list:
    sentence.append(letters.index(letter))

print(sentence)