from PIL import Image

BiggerImg = Image.open("41.jpg")
SmallerImg = Image.open("hack.png")

# //Line 1 : The area of smaller image to be superimposed is taken i.e. if small img is 200x200
#  //Line 2 : Area start from min 0,0,200,200 or max 1600-200 =1400,900-200=700 to fit on the bigger one

area = (600, 200, 800, 400)
BiggerImg.paste(SmallerImg, area)

BiggerImg.show()
