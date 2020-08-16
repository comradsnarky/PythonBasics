while True:

    month = input('Enter the number of the month: ')

    if month.isdigit():
        month = int(month)
        my_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                   5: 'May', 6: 'June', 7: 'July', 8: 'August',
                   9: 'September', 10: 'October',
                   11: 'November', 12: 'December', 13: 'Winter',
                   14: 'Spring', 15: 'Summer', 16: 'Autumn'}

        if month == 1 or month == 2 or month == 12:
            season = 13
        elif month == 3 or month == 4 or month == 5:
            season = 14
        elif month == 6 or month == 7 or month == 8:
            season = 15
        else:
            season = 16

        if month == 1:
            print(f'\nThe {month}-st month is {my_dict.get(month)} and'
                  f' it\'s in {my_dict.get(season)}.')
        elif month == 2 or month == 3:
            print(f'\nThe {month}-d month is {my_dict.get(month)} and'
                  f' it\'s in {my_dict.get(season)}.')
        elif month == 0 or month > 12:
            print('The number of the month should be > 0 and < 13!\n')
            continue
        else:
            print(f'\nThe {month}-th month is {my_dict.get(month)} and'
                  f' it\'s in {my_dict.get(season)}.')
        break

    else:
        print('The number of the month should be > 0 and < 13!\n')
