


from PIL import Image, ImageFilter


im = Image.open("dog.jpg")
im = im.resize((150,150))
blure = im.filter(ImageFilter.GaussianBlur(3))
blure.show()