


from PIL import Image


im = Image.open("dog.jpg")

image_file = im.convert('1') # convert image to black and white
image_file.save('dogBW.png')
image_file.show()