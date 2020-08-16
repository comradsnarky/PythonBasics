number = int(input('Enter a random whole number: '))

biggerNumber = 0

while number > 0:
    if biggerNumber < (number % 10):
        biggerNumber = (number % 10)
        number = number // 10
    elif biggerNumber == 9:
        break
    else:
        number = number // 10

print(biggerNumber)
