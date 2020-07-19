genList1 = [el for el in range(20, 241) if el % 20 == 0]
genList2 = [el for el in range(20, 241) if el % 21 == 0]

print(f'Generated list of numbers whose aliquot part is 20: {genList1}')
print(f'Generated list of numbers whose aliquot part is 21: {genList2}')
