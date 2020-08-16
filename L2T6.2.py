originalList = [(1, {'name': 'Desktop computer', 'price': 20000, 'quantity': 5, 'unit': 'set'}),
                (2, {'name': 'Printer', 'price': 6000, 'quantity': 2, 'unit': 'pcs'}),
                (3, {'name': 'Scanner', 'price': 2000, 'quantity': 7, 'unit': 'pcs'}),
                (4, {'name': 'Keyboard', 'price': 1000, 'quantity': 10, 'unit': 'pcs'}),
                (5, {'name': 'Keyboard', 'price': 1500, 'quantity': 7, 'unit': 'pcs'}),
                (6, {'name': 'Keyboard+mouse', 'price': 2000, 'quantity': 5, 'unit': 'set'})]

dictList = []
nameList = []
priceList = []
quantityList = []
measureList = []
tempDict = ()
myDict = {}
consolidDict = {}

for i in range(len(originalList)):
    dictList.append(originalList[i][1])

for n in range(len(dictList)):
    myDict = dictList[n]
    nameList.append(myDict['name'])
    priceList.append(myDict['price'])
    quantityList.append(myDict['quantity'])
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
