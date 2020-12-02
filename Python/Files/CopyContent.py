"""
Copy content file to file
"""

with open("file.txt","r") as read_file:
    content_file = read_file.read()

with open("copied.txt",'w') as write_file: #object file to write
    for letter in content_file:
        write_file.write(letter)