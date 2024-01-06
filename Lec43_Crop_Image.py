from PIL import Image

img = Image.open("41.jpg")

# Open image in paint and select the area to crop and then read the area or dimension
# dimensions can be read at Top-left and Bottom Right corner for accurate area
area = (510, 4, 1128, 900)
cropped = img.crop(area)

img.show()
cropped.show()
