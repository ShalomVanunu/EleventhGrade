"""
this program sort the content
"""

with open("fileTR2.txt", 'r') as read_file:
    content = read_file.read()
    content = content.lower()

list_of_word = content.split(" ")
sorted_list = sorted(list_of_word)
print(sorted_list)