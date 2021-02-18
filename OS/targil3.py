import os
import threading

def burgerking(file):
	command = input("Enter a command for the os \n")
	cm = os.popen(command).read()
	print(cm)
	file.write(cm + "\n")

def main():
	threads = []
	file = open("Y.txt",'w+')
	file.write('') # earase all the info in the file (if you run in twice)
	for x in range(5):
		m = (threading.Thread(target = burgerking, args = (file,)))
		threads.append(m.start())
		m.join()
main()