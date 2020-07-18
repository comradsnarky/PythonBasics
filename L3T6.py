def int_func(line):
    capitalized = line.title()
    return print(f'{line} --> {capitalized}')

line = 'text'
int_func(line)

line = input('\nEnter a word in lower case: ')
int_func(line)
