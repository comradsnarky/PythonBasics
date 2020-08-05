class MyClass:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        a = complex(self.__dict__.get('num_1'), self.__dict__.get('num_2'))
        b = complex(other.__dict__.get('num_1'), other.__dict__.get('num_2'))
        res = a + b
        return print(f'{a} + {b} = {res}')

    def __mul__(self, other):
        a = complex(self.__dict__.get('num_1'), self.__dict__.get('num_2'))
        b = complex(other.__dict__.get('num_1'), other.__dict__.get('num_2'))
        res = a * b
        return print(f'{a} * {b} = {res}')

from random import randint as rn

my_1 = MyClass(rn(1, 10), rn(1, 10))
print(f'First complex number: {my_1.__dict__.get("num_1")}+{my_1.__dict__.get("num_2")}j')
my_2 = MyClass(rn(1, 10), rn(1, 10))
print(f'Second complex number: {my_2.__dict__.get("num_1")}+{my_2.__dict__.get("num_2")}j')


sum = my_1 + my_2
mul = my_1 * my_2
