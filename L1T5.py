income = int(input('Enter your company\'s income: '))
expenditure = int(input('Enter your company\'s expenditure: '))

if income > expenditure:
    profitability = int(((income / expenditure) * 100))
    print(f'\nCongratulations, you have a profitable business!\n'
          f'Your company\'s profitability equals {profitability}%\n')
    stuff = int(input('Enter the number of company\'s employees: '))
    print(f'\nCompany\'s profitability by employee equals '
          f'{round((profitability / stuff), 2)}% per employee')
elif income == expenditure:
    print('\nThere\'s no profit in your company. You\'re barely '
          'making ends meet.')
else:
    print('\nUnfortunately, your company is not doing very well.')
