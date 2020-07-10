userWords = input('Enter several random words divided by blank: ')

userWords = userWords.split()

for i in range(len(userWords)):
    if len(userWords[i]) > 10:
        element = userWords[i]

        if i == 0:
            print(f'{i + 1}-st element of the list - {element[:10]}')
        elif i == 1 or i == 2:
            print(f'{i + 1}-d element of the list - {element[:10]}')
        else:
            print(f'{i + 1}-th element of the list - {element[:10]}')

    else:
        if i == 0:
            print(f'{i + 1}-st element of the list - {userWords[i]}')
        elif i == 1 or i == 2:
            print(f'{i + 1}-d element of the list - {userWords[i]}')
        else:
            print(f'{i + 1}-th element of the list - {userWords[i]}')
