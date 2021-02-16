
import os

# bring the currect dirctory
currect_dir = os.getcwd()
print(currect_dir)

# make dir
try:
    os.mkdir("class")
except:
    pass # dont do anything

# go to directory class
os.chdir("class")
with open("test.txt", "w") as write: # w - overwrite || a- append
    write.write("")
isexsist = os.path.isfile("test.txt")
print(isexsist)