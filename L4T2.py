my_list = []
import random
for i in range(10):
    my_list.append(random.randint(1, 1000))
genList = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(f'Original list: {my_list}')
print(f'Generated list: {genList}')
