class Mario:

    @staticmethod
    def move():
        print("I am moving")


class Shroom:

    @staticmethod
    def eat_shroom():
        print("Now I am bigger")


class BigMario(Mario, Shroom):
    pass


bm = BigMario()
bm.move()
bm.eat_shroom()
