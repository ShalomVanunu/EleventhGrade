
import os

path = input("Enter your PATH \n")
file = input("Enter the file you search \n")
#path = os.getcwd() # get the current directory
for dirpath,dirnames,filenames in os.walk(path):
   #print(dirpath)
  # for file in filenames:
  #     print(file)
 #  print("__________________________")
 if file in filenames:
     print("the file found", file)



