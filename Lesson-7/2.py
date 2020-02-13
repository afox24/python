class Dress:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_s(self):
        return self.height * 2 + 0.3

    @property
    def get_square_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Dress):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'

class Suit(Dress):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_s}'

coat = Coat(50, 30)
suit = Suit(10, 15)
print(coat)
print(suit)
print(coat.get_square_full)
print(suit.get_square_full)
print(suit.get_square_c())
print(suit.get_square_s())


