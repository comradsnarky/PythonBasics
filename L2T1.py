my_list = ['string', 4, 5.8, False, 2+3j, None]

print(f'List: {my_list}\n')

for i in range(len(my_list)):
    print(f'Type of the {i + 1} element is {type(my_list[i])}')
