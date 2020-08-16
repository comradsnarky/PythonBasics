def my_func1(x, y):
    result = 1 / (x**(y * -1))
    return print(f'{x} to the power of {y} equals: {result:.2}')

def my_func2(x, y):
    power = x
    for i in range(1, y * -1):
        power = power * x
    result = 1 / power
    return print(f'{x} to the power of {y} equals: {result:.2}')

x = 4
y = -4

my_func1(x, y)
my_func2(x, y)
