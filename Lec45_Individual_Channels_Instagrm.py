from PIL import Image

BiggerImg = Image.open("41.jpg")

print(BiggerImg.mode)


r, g, b = BiggerImg.split()
r.show()
g.show()
b.show()
