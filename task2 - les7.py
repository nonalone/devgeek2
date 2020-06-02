class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def amount_textile_coat(self):
        return self.width / 6.5 + 0.5

    def amount_textile_jacket(self):
        return 2 * self.height + 0.3

    @property
    def amount_full_textile(self):
        return f'Общее количество метров ткани на одежду {round(self.width / 6.5 + 0.5) + (2 * self.height + 0.3)}'


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.amount_textile_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Метров ткани на пальто {self.amount_textile_coat}'


class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.amount_textile_jacket = round(2 * self.height + 0.3)

    def __str__(self):
        return f'Метров ткани на пиджак {self.amount_textile_jacket}'


coat = Coat(7, 3)
jacket = Jacket(3, 3)
print(jacket)
print(coat)
print(jacket.amount_full_textile)
print(coat.amount_full_textile)