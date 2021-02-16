""" this example RUN process like in command """
import os

os.system("whoami") # run the process and show the result on screen

command_result = os.popen("whoami").read() # run the process and svae the result in argument
print(command_result)

systeminfo = os.popen("systeminfo").readlines()
print(systeminfo[3])

