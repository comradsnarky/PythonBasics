my_f = open('text_6.txt', 'r', encoding='utf-8')

content = my_f.readlines()
my_dict = {}

for i in range(len(content)):
    hours = ''
    sum = 0
    subContent = list(content[i])
    keys = content[i].split()
    for n in range(len(subContent)):
        if subContent[n].isdigit() and subContent[n + 1].isdigit():
            hours += subContent[n]
        elif subContent[n].isdigit() and subContent[n + 1].isdigit != True:
            hours += subContent[n] + ' '
        else:
            pass
    for k in hours.split():
        sum += int(k)
    my_dict.update({keys[0][:-1]: sum})
print(my_dict)
