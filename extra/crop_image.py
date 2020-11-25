from PIL import Image
import PIL
import os

os.system("dir")
image = input("Image to resize: ")
im = Image.open(image)
width, height = im.size

print(width, height)
if height > 1000:
	x = height//1000
	width = width//(x+1)
	height = height//(x+1)
im1 = im.resize((width, height))
width, height = im1.size
print(width, height)
im1 = im1.save("C:\\Users\\Admine\\Desktop\\maskProgram\\new\\Face-Mask-Detection\\images\\image.jpg")
