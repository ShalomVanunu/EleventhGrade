

from PIL import Image


im = Image.open("dog.jpg")
im.rotate(45).show()