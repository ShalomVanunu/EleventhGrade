"""
this program make password code by the lengh of the user
"""

import random

# this function create list of all words from file
def get_words_from_file():
    with open("words.txt","r") as reader:
        pagelist = reader.read().split('\n')
    return pagelist

# create 3 random words from list of words
def get_random_words(pagelist):
    random_words = ""
    for word in range(3):
        random_words += random.choice(pagelist)
    return random_words # 3 words together

# create password from the 3 words
def make_password(length):
    random_words = get_random_words(get_words_from_file())
    password = ""
    for letter in range(length):
        password += random_words[random.randint(0,len(random_words))]
    return password


if __name__ == "__main__":
    lenght = int(input("Please enter the lengh of the password"))
    print(make_password(lenght))