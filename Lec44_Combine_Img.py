from PIL import Image

BiggerImg = Image.open("41.jpg")
SmallerImg = Image.open("hack.png")

area = (600, 200, 800, 400)
BiggerImg.paste(SmallerImg, area)

BiggerImg.show()
