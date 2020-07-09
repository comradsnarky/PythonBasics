lengthList = int(input('Enter the number of elements in the list: '))
userList = []
swappedUserList = []

for i in range(lengthList):
    userList.append(input(f'Enter the {i + 1} element of the list: '))
    if i % 2 == 0:
        swappedUserList.insert((i + 1), userList[i])
    else:
        swappedUserList.insert((i - 1), userList[i])

print(f'\nOriginal list: {userList}')
print(f'List with swapped elements: {swappedUserList}')
