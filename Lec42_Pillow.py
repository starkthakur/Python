from PIL import Image
img = Image.open("41.jpg")
print(img.size)
print(img.mode)
print(img.format)
print(img.info)

img.show()
