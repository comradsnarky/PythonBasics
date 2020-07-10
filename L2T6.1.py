originalList = [(1, {'name': 'Desktop computer', 'price': 20000, 'quantity': 5, 'unit': 'set'}),
                (2, {'name': 'Printer', 'price': 6000, 'quantity': 2, 'unit': 'pcs'}),
                (3, {'name': 'Scanner', 'price': 2000, 'quantity': 7, 'unit': 'pcs'}),
                (4, {'name': 'Keyboard', 'price': 1000, 'quantity': 10, 'unit': 'pcs'}),
                (5, {'name': 'Keyboard', 'price': 1500, 'quantity': 7, 'unit': 'pcs'}),
                (6, {'name': 'Keyboard+mouse', 'price': 2000, 'quantity': 5, 'unit': 'set'})]

dictList = []
nameList = ['Desktop computer']
priceList = [20000]
quantityList = [5]
measureList = ['set']
tempDict = ()
myDict = {}
consolidDict = {}

for i in range(len(originalList)):
    dictList.append(originalList[i][1])

for n in range(len(dictList)):
    myDict = dictList[n]
    if nameList.count(myDict['name']) <= 0:
        nameList.append(myDict['name'])
    if priceList.count(myDict['price']) <= 0:
        priceList.append(myDict['price'])
    if quantityList.count(myDict['quantity']) <= 0:
        quantityList.append(myDict['quantity'])
    if measureList.count(myDict['unit']) <= 0:
        measureList.append(myDict['unit'])

    if n == 0:
        myDict.popitem()
        myDict.popitem()
        myDict.popitem()
        tempDict = myDict.popitem()
        consolidDict.update({tempDict[0]: nameList})
    elif n == 1:
        myDict.popitem()
        myDict.popitem()
        tempDict = myDict.popitem()
        consolidDict.update({tempDict[0]: priceList})
    elif n == 2:
        myDict.popitem()
        tempDict = myDict.popitem()
        consolidDict.update({tempDict[0]: quantityList})
    else:
        tempDict = myDict.popitem()
        consolidDict.update({tempDict[0]: measureList})

print(f'{consolidDict}\n')

print('\n'.join("'{}': {}".format(k, v) for k, v in consolidDict.items()))
