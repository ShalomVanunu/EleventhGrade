import os
try:
    os.mkdir("OS")
except:
    pass
os.chdir("OS")
try:
    os.mkdir("Product")
except:
    pass
with open("Text.txt", "w") as write:
    write.write("")
try:
    os.system(r"copy Text.txt c:\Users\Public\Downloads\OS\Product")
except:
    pass
try:
    os.remove("Text.txt")
except:
    pass
isexsist = os.path.isfile("Text.txt")
print(isexsist)


