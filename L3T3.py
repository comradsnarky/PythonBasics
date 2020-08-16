def num_gen():
    import random
    random_num = random.randint(1, 100)
    return random_num

def compare_func(numList):
    numList = sorted(numList)
    return print(f'The smallest number is {numList[0]}.'
                 f'\nThe sum of the two biggest ones equals: {numList[1] + numList[2]}')

def manual_num():
    i = 1
    while i < 4:
        num = input(f'Press Q to quit program.\nEnter {i} number: ').lower()
        try:
            if num == 'q':
                print('It was fun! See ya!')
                quit()
            num = int(num)
            numList.append(num)
            i += 1
        except ValueError:
            print('You should enter a number!')
    return numList

while True:
    choice = input('Would you like to generate numbers or enter them manually?'
               '\nPress A for automatic, M for manual, Q to quit program: ').lower()
    if choice == 'a' or choice == 'm' or choice == 'q':
        break
    else:
        print('Press A, M or Q!')
        continue


numList = []

if choice == 'm':
    manual_num()
    print(f'Numbers you\'ve entered are: {tuple(numList)}')
    compare_func(numList)
elif choice == 'a':
    for i in range(3):
        numList.append(num_gen())
    print(f'Random generated numbers are: {tuple(numList)}')
    compare_func(numList)
elif choice == 'q':
    print('It was fun! See ya!')
    quit()
