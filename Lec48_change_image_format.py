from PIL import Image
from PIL import ImageFilter

john = Image.open("42.png")
black_white = john.convert("L")
blur = john.filter(ImageFilter.GaussianBlur(5))
detail = john.filter(ImageFilter.DETAIL)
edges = john.filter(ImageFilter.FIND_EDGES)

black_white.show()
blur.show()
detail.show()
edges.show()
