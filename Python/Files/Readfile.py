f = open("file.txt","r") # this store the file object
read_file = f.readlines() # reads the content of the file into variable
print(read_file[2])
f.close()

print("--------------------------------")
f = open("file.txt","r") # this store the file object
read_file = f.read() # reads the content of the file into variable
print(read_file)
f.close() # close file

if 'shalom' in read_file:
    print(True)
else:
    print(False)