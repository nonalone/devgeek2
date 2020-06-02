class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Cell amount {self.amount * "*"}'

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return Cell(self.amount - other.amount)
        else:
            return 'Wrong number! (-)'

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(round(self.amount // other.amount))

    def make_order(self, cell_amount_in_row):
        row = ' '
        for i in range(int(self.amount / cell_amount_in_row)):
            row += f'{"*" * cell_amount_in_row} \\n'
        row += f'{"*" * (self.amount % cell_amount_in_row)}'
        return row

cell1 = Cell(12)
cell2 = Cell(5)
print(cell1)
print(cell1 * cell2)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 / cell2)
print(cell1.make_order(3))
print(cell1.make_order(5))
