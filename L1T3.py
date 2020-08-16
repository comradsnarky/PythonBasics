number = int(input('Enter a random number: '))

concatNumber1 = int(f'{number}{number}')
concatNumber2 = int(f'{number}{number}{number}')

print(f'\nSum of {number} + {concatNumber1} + '
      f'{concatNumber2} = '
      f'{(number + concatNumber1 + concatNumber2)}')
