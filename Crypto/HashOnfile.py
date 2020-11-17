

import hashlib

with open("dog.jpg",'rb') as reader :
    dog_binary = reader.read()

hash = hashlib.md5(dog_binary)
print("Original")
print(hash.hexdigest())

with open("dogcahnged.jpg",'rb') as reader :
    dog_binary = reader.read()

hash = hashlib.md5(dog_binary)
print("Changed")
print(hash.hexdigest())