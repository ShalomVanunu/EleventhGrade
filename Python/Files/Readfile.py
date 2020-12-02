f = open("file.txt","r") # this store the file object
read_file = f.readlines() # reads the content of the file into variable
print(read_file[2])
f.close()

print("-----------Option1---------------------")
read_file = open("file.txt","r") # this store the file object
content_file = read_file.read() # reads the content of the file into variable
print(content_file)
read_file.close() # close

print("-----------Option2---------------------")
read_file = open("file.txt","r") # this store the file object
content_file = read_file.readlines() # reads the lines content of the file into variable
print(content_file[1])
read_file.close() # close file

print("-----------Option3---------------------")

with open("file.txt","r") as read_file:
    content_file = read_file.readlines()

for line in content_file:
    if "Covid" in line:
        print(line)