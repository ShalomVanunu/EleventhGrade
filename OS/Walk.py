
import os
path = os.getcwd() # get the current directory
for dirpath,dirnames,filenames in os.walk(path):
   print(dirpath)
   for file in filenames:
       print(file)
   print("__________________________")

