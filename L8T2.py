class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

in_data = input('Enter a number ≠ 0: ')

try:
    in_data = int(in_data)
    if in_data == 0:
        raise MyError('Division by zero is impossible!')
except ValueError:
    print('Enter a number not string!')
except MyError as err:
    print(err)
else:
    res = 46987 / in_data
    print(f'{res:.2f}')
