class Stationery:
    def __init__(self, title):
        self.titile = title

    def draw(self):
        print('Запуск отрисовки! ')

class Pen(Stationery):
    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        print(f'У вас в руках {self.titile} запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У вас в руках {self.titile} запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У вас в руках {self.titile} запуск отрисовки маркером')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
a = Stationery(' ')
a.draw()
pen.draw()
pencil.draw()
handle.draw()
