
"""
ab....zAB...Z
"""
import string
#
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
#
shift = 1
# letter = 'z'
# # use ASCII table
# print(chr(((ord(letter)+shift-97)%26)+97))
# #      number in ascii table+shift

with open('Time to vote America.txt', 'r') as reader:
    content = reader.read()

strings = string.ascii_lowercase # abc...yz 26 characters

new_sentence = ""
for letter in content.lower() :

    if letter == " ":
        new_sentence +=' '
    else:
        # user strings
        number=((strings.index(letter)+shift)%26)
        new_sentence +=(strings[number])

print(content)
print(new_sentence)