
"""
program that print what you enter until you press Q to exit
"""

while True :
    key_input = input("enter what on your mind [Q to exit]:")
    if key_input.lower() == "q":
        break
    print(key_input)