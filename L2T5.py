my_list1 = [20, 15, 15, 14, 12, 10, 9, 7, 5, 3, 3, 2]

userNumber = float(input('Enter a random number: '))

ind = 0
for i in range(len(my_list1)):
    if userNumber > my_list1[i]:
        ind = i
        break
    elif userNumber <= my_list1[-1]:
        ind = i + 1
    elif userNumber == my_list1[i] and my_list1[i] != my_list1[i + 1]:
        ind = i + 1
        break
    else:
        ind = i

my_list1.insert(ind, userNumber)

print(my_list1)
