userTime = int(input('Enter time in seconds: '))

minute = userTime // 60
second = userTime % 60
hour = minute // 60
minute = (userTime // 60) % 60

print(f'\nYour time in hh:mm:ss format: '
      f'{hour:02}:{minute:02}:{second:02}')
