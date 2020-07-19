from sys import argv
name, hours, salPerHour, bonus = argv
print(f'For {int(float(hours) // 1)} hours and {round(60 * (float(hours) % 1))} '
      f'minutes, salary is {(float(hours) * float(salPerHour)) * float(bonus):.2f}, '
      f'including {int((float(bonus) * 100) - 100)}% bonus')
