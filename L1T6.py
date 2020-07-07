userDistance = float(input('Enter distance of the first training '
                         'session: '))

print(f'\n1-st day: {userDistance}km')

dayCounter = 1

while userDistance < 3:
    if userDistance >= 3:
        break
    userDistance = userDistance * 1.1
    dayCounter += 1
    if dayCounter == 2 or dayCounter == 3 or dayCounter == 22 or \
            dayCounter == 23 or dayCounter == 32 or dayCounter == 33:
        print(f'{(dayCounter)}-d day: {round(userDistance, 2)}km')
    elif dayCounter == 21 or dayCounter == 31:
        print(f'{(dayCounter)}-st day: {round(userDistance, 2)}km')
    else:
        print(f'{(dayCounter)}-th day: {round(userDistance, 2)}km')

if dayCounter == 2 or dayCounter == 3 or dayCounter == 22 or \
        dayCounter == 23 or dayCounter == 32 or dayCounter == 33:
    print(f'\nWith 10% increment you\'ll be able to run at least 3km '
          f'on the {dayCounter}-d day')
elif dayCounter == 21 or dayCounter == 31:
    print(f'\nWith 10% increment you\'ll be able to run at least 3km '
          f'on the {dayCounter}-st day')
elif dayCounter == 1:
    print('\nCongratulations, you\'re already capable of '
          'running at least 3km!')
else:
    print(f'\nWith 10% increment you\'ll be able to run at least 3km '
          f'on the {dayCounter}-th day')
