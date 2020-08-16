def my_func1(userNum):
    global numList
    numList = userNum.split()
    for i in numList:
        if i.isdigit():
            continue
        elif i == 'q':
            result = 0
            numList.remove(i)
            for n in numList:
                result = result + int(n)
            if len(numList) == 1:
                print(f'\nThe sum equals: {result}.')
            else:
                print(f'\nThe sum of numbers {tuple(numList)} equals: {result}.')
            quit()
        else:
            numList.remove(i)
            userNum = (' '.join("{} ".format(k) for k in numList)) + input('Enter only numbers: ')
            my_func1(userNum)
    my_func2(numList)

def my_func2(numList):
    global result
    result = 0
    for i in numList:
        result = result + int(i)
    return my_func3()

def my_func3():
    userNum = (f'{result} ') + input(f'\nThe sum of numbers {tuple(numList)} equals: {result}.'
                                     f'\nIf you want to continue, just keep on entering numbers divided by a blank.'
                                     f'\nIf not, press Q to quit the program: ').lower()
    my_func1(userNum)

userNum = input('Enter several numbers separated by a blank: ')
my_func1(userNum)
