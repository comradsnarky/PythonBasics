import math as m

my_list = []

def gen():
    for el in [el for el in range(1, 8)]:
        if el == 1:
            my_list.append(el)
            print(f'{el}! = {m.factorial(el)}')
            yield el
        elif el < 6:
            my_list.append(el)
            print(f'{el}! = {" * ".join("{}".format(k) for k in my_list)} = {m.factorial(el)}')
            yield el
        else:
            print(f'{el}! = {" * ".join("{}".format(k) for k in my_list)} ... = {m.factorial(el)}')
            yield el

for i in gen():
    pass
