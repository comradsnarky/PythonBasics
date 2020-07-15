def my_func1(keys):
    for i in range(len(keys)):
        personalInfo.update({keys[i]: input(f'Enter your {keys[i]}: ')})
    return print(f'\nYou entered following information:\n'
                 f'{", ".join("{} - {}".format(k.title(), v) for k, v in personalInfo.items())}')

def my_func2():
    i = 0
    for n, m in personalInfo.items():
        if m == i:
            keys.append(n)
            i += 1
    return keys


personalInfo = {
    'name': 0, 'last name': 1, 'year of birth': 2,
    'city of residence': 3, 'e-mail': 4, 'phone number': 5
}

keys = []

my_func2()
my_func1(keys)
