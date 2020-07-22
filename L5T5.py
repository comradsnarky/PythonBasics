my_f = open('text_5.txt', 'w', encoding='utf-8')

sum = 0
import random
for i in range(10):
    ranNum = random.randint(1, 100)
    sum += ranNum
    my_f.write(f'{ranNum} ')
my_f.close()

my_f1 = open('text_5.txt', 'r', encoding='utf-8')

print(f'Sum of numbers {tuple(my_f1.readline().split())} = {sum}')



