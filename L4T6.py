import itertools as it
for el in it.count(3):
    if el > 10:
        break
    else:
        print(el)

print('\n')

c = 0
for el in it.cycle([1, 'str', 3 * 5j, [1, 2], (1, 2), {1, 2}]):
    if c > 10:
        break
    else:
        print(type(el))
        c += 1
