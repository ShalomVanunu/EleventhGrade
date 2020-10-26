from PIL import Image


im = Image.open("dog.jpg")
im = im.resize((50,50))
im.show()

