"""
this exercise read from file.and write in Reversed Mode
"""

# read the content of file
with open("file.txt", "r") as reader:
    data_reader = reader.read()

# write to file
with open("reversedfile.txt", "w") as writer: # create the file & object
    data_reader_revered = data_reader[::-1]
    writer.write(data_reader_revered)
    #for line in reversed(data_reader):
     #   writer.write(line)