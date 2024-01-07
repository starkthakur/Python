from PIL import Image

john = Image.open("41.jpg")
hack = Image.open("wp2.jpg")

''''
print(BiggerImg.mode)
r, g, b = BiggerImg.split()
# Play with the band input i.e. instead of r, g, b use b ,g, r to get a bluish img
newImg = Image.merge("RGB", (b, g, r))

'''
r, g, b = john.split()
r1, g1, b1 = hack.split()

newImg = Image.merge("RGB", (r1, g1, b))
newImg.show()
