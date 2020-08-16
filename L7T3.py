from os import linesep as ls
class Cell:
    def __init__(self, name, cell_num, order):
        self.name = name
        self.cell_num = cell_num
        self.order = order
        print(f'{self.name}: {"*" * self.cell_num}')

    def __add__(self, other):
        cell_sum = self.__dict__.get('cell_num') + other.__dict__.get('cell_num')
        self.cell_num = cell_sum
        return self.cell_num

    def __sub__(self, other):
        cell_sub = self.__dict__.get('cell_num') - other.__dict__.get('cell_num')
        if cell_sub < 0:
            print('Subtraction is negative! Objects have been swapped places!')
            cell_sub = other.__dict__.get('cell_num') - self.__dict__.get('cell_num')
        self.cell_num = cell_sub
        return self.cell_num

    def __mul__(self, other):
        cell_mul = self.__dict__.get('cell_num') * other.__dict__.get('cell_num')
        self.cell_mul = cell_mul
        return self.cell_mul

    def __truediv__(self, other):
        cell_div = self.__dict__.get('cell_num') // other.__dict__.get('cell_num')
        if cell_div < 1:
            print('Division result is less than 1! Objects have been swapped places!')
            cell_div = other.__dict__.get('cell_num') // self.__dict__.get('cell_num')
        self.cell_div = cell_div
        return self.cell_div

    def make_order(self):
        my_list = []
        row = self.cell_num // self.order
        remainder = self.cell_num % self.order
        for i in range(row):
            my_list.append('*' * self.order)
        if remainder > 0:
            my_list.append('*' * remainder)
        return self.name, my_list

cell_1 = Cell('obj_1', 12, 5)
print(f'Ordered {cell_1.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_1.make_order()[1])}')

print()
cell_2 = Cell('obj_2', 15, 6)
print(f'Ordered {cell_2.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_2.make_order()[1])}')

print()
cell_3 = Cell('obj_3', cell_1 + cell_2, 8)
print(f'Ordered {cell_3.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_3.make_order()[1])}')

print()
print('- ' * 20)
print()

cell_4 = Cell('obj_4', 7, 6)
print(f'Ordered {cell_4.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_4.make_order()[1])}')

print()
cell_5 = Cell('obj_5', 10, 6)
print(f'Ordered {cell_5.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_5.make_order()[1])}')

print()
cell_6 = Cell('obj_6', cell_4 - cell_5, 8)
print(f'Ordered {cell_6.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_6.make_order()[1])}')

print()
print('- ' * 20)
print()

cell_7 = Cell('obj_7', 7, 6)
print(f'Ordered {cell_7.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_7.make_order()[1])}')

print()
cell_8 = Cell('obj_8', 10, 6)
print(f'Ordered {cell_8.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_8.make_order()[1])}')

print()
cell_9 = Cell('obj_9', cell_7 * cell_8, 15)
print(f'Ordered {cell_9.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_9.make_order()[1])}')

print()
print('- ' * 20)
print()

cell_10 = Cell('obj_10', 5, 15)
print(f'Ordered {cell_10.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_10.make_order()[1])}')

print()
cell_11 = Cell('obj_11', 67, 15)
print(f'Ordered {cell_11.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_11.make_order()[1])}')

print()
cell_12 = Cell('obj_12', cell_10 / cell_11, 5)
print(f'Ordered {cell_12.make_order()[0]}:\n{ls.join("{}".format(v) for v in cell_12.make_order()[1])}')
