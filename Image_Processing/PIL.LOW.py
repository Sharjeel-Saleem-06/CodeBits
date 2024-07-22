from PIL import Image, ImageOps , ImageDraw , ImageFont , ImageFilter

image=Image.open("D:\python.py\Mini_Projects\CodeBits\Image_Processing\images.jpeg"),
# image.show()

# Methos related image information
# print(image.info)
# print(image.size)
# print(image.mode)
# print(image.format)

# To save image
# image.save("example.png")

# Image Operations
# ImageOps is used to perform operation on image
# image1=ImageOps.flip(image)
# image2=ImageOps.mirror(image)
# image3=ImageOps.grayscale(image)
# image4=ImageOps.invert(image)
# image4.show()

# Image Transformations
# image5=image.resize((100,100))
# image_draw1=ImageDraw.Draw(image)
# font = ImageFont.truetype("arial.ttf", size=36)
# image_draw1.text((28,36), "HEllo World!",font=font, fill=(255,255,255))
# image.show()

# Crop and Paste
# box=(20,10,570,570)  # (20, 10) is the top-left corner of the rectangle.  # (570, 570) is the bottom-right corner of the rectangle.
# image_crop=image.crop(box)
# image_crop.show()
# image.paste(image_crop,(0,0))
# image.paste(image_crop,(340,0)) # we can add second img here so that both pic are in 1 frame just replace name with image_crop
# image.show()

b=image.filter(ImageFilter.BLUR)
b.show()
