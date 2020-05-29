class Road:
    def __init__(self, _length, _width, thikness, massonmeter):
        self._length = _length
        self._width = _width
        self.thikness = thikness
        self.massonmeter = massonmeter

    def mass(self):
        return self._length * self._width * self.thikness * self.massonmeter


class Mass(Road):
    def __init__(self, _length, _width, thikness, massonmeter):
        super().__init__(_length, _width, thikness, massonmeter)
        print('Need for road ')


r = Mass(20, 5000, 25, 5)
print(r.mass(), 'kg')
