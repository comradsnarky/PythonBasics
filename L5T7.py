my_f = open('text_7.txt', 'r', encoding='utf-8')

content = my_f.readlines()
profit_dict = {}
average_dict = {}
loss_dict = {}
avr = 0
counter = 0

for i in range(len(content)):
    if content[i][-1].isdigit() != True:
        companies = content[i][:-1].split()
        income = int(companies[2])
        expenditure = int(companies[3])
    else:
        companies = content[i].split()
        income = int(companies[2])
        expenditure = int(companies[3])
    if expenditure < income:
        counter += 1
        avr += income - expenditure
        profit_dict.update({companies[0]: income - expenditure})
    else:
        loss_dict.update({companies[0]: income - expenditure})

my_f.close()

average_dict.update({'average_profit': avr/counter})

my_list = [profit_dict, average_dict, loss_dict]
print(my_list)

import json
with open('text_7.1.json', 'w', encoding='utf-8') as my_json:
    json.dump(my_list, my_json, ensure_ascii=False, indent=4)
my_json.close()
