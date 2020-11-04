

with open('Time to vote America.txt', 'r') as reader:
    content = reader.read()

draw_back = content[::-1]
print(content)
print("_________________________________________________")
print(draw_back)