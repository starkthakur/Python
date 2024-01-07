from PIL import Image

john = Image.open("42.png")
square = john.resize((800, 800))
flip = john.transpose(Image.FLIP_LEFT_RIGHT)
spin = john.transpose(Image.ROTATE_90)

john.show()
square.show()
flip.show()
spin.show()
