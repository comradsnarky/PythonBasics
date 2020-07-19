my_list = []
import random
for i in range(30):
    my_list.append(random.randint(1, 20))

genList = [el for el in my_list if my_list.count(el) == 1]

print(my_list)
print(genList)
