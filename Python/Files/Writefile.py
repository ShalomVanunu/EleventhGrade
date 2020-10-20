
text = "today is Tuesday the 20th of October 2020\n "
file_write = open("wfile.txt" ,"a+")
file_write.write(text)
file_write.close()

print("----------------------------------")

text = "New Data"
file_write = open("wfile.txt" ,"a+")
file_write.write(text)
file_write.close()

with open("wfile.txt","r+") as r :
    print(r.read())