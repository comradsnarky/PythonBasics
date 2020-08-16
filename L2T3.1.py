while True:
    month = input('Enter the number of the month: ')
    if month.isdigit():
        month = int(month)
        my_list = [['Winter', 'January'], ['Winter', 'February'],
                   ['Spring', 'March'], ['Spring', 'April'],
                   ['Spring', 'May'], ['Summer', 'June'],
                   ['Summer', 'July'], ['Summer', 'August'],
                   ['Autumn', 'September'], ['Autumn', 'October'],
                   ['Autumn', 'November'],  ['Winter', 'December']]

        if month == 1:
            print(f'\nThe {month}-st month is {my_list[month - 1][1]} and it\'s in'
                  f' {my_list[month - 1][0]}.')
        elif month == 2 or month == 3:
            print(f'\nThe {month}-d month is {my_list[month - 1][1]} and it\'s in'
                  f' {my_list[month - 1][0]}.')
        elif month == 0 or month > 12:
            print('The number of the month should be > 0 and < 13!\n')
            continue
        else:
            print(f'\nThe {month}-th month is {my_list[month - 1][1]} and it\'s in'
                  f' {my_list[month - 1][0]}.')
        break
    else:
        print('The number of the month should be > 0 and < 13!\n')
