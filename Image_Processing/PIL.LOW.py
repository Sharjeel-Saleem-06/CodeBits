from PIL import Image, ImageOps

image=Image.open("D:\python.py\Mini_Projects\CodeBits\Image_Processing\images.jpeg")
# image.show()

# Methos related image information
# print(image.info)
# print(image.size)
# print(image.mode)
# print(image.format)

# To save image
image.save("example.png")

# Image Operations
# ImageOps is used to perform operation on image
image1=ImageOps.flip(image)
image2=ImageOps.mirror(image)
image3=ImageOps.grayscale(image)
image4=ImageOps.invert(image)
image4.show()

# Image Transformation
