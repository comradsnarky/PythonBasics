def wage():
    sum = 0
    for i, n in my_dict.items():
        salary = float(n)
        sum += salary
        if salary < 20000:
            print(f'{i} - {n}')
    avr = sum / len(my_dict)
    return avr

my_f = open('text_3.txt', 'r', encoding='utf-8')
content = my_f.readlines()

my_dict = {}
for i in range(len(content)):
    _ = content[i].split()
    my_dict.update({_[0]: _[1]})

print(f'Following employees have salary less than 20000:')
print(f'\nAverage salary is: {wage()}')
my_f.close()
