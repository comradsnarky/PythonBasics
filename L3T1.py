def my_func1(num1, num2):
    try:
        division = num1 / num2
        return print(f'{num1} / {num2} = {division:.3f}')
    except ZeroDivisionError:
        print('Division by zero is not acceptable!')

def my_func2():
    i = 1
    while True:
        num = input(f'Enter {i} number: ')
        try:
            num = float(num)
            numList.append(num)
            i += 1
            if i > 2:
                return numList
        except ValueError:
            print('You should enter a number!')

numList = []
my_func2()
my_func1(numList[0], numList[1])
