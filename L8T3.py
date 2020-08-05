class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

print('To stop the program press Q')
while True:
    in_data = input('Enter a number: ').lower()
    try:
        if in_data.isdigit() == False and in_data != 'q':
            raise MyError('Enter only numbers!')
        elif in_data == 'q':
            print(my_list)
            quit()
    except MyError as err:
        print(err)
    else:
         my_list.append(in_data)
