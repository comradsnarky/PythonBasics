import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            print(f'\033[101m')
        elif self.__color == 'yellow':
            print(f'\033[103m')
        else:
            print(f'\033[102m')

my_list = [['red', 5], ['yellow', 2], ['green', 7]]
i = 0
n = 0
while True:
    traffic_light = TrafficLight(my_list[i][0])
    traffic_light.running()
    print('\n' * 10)
    time.sleep(my_list[i][1])
    i += 1
    n += 1
    if i == 3:
        i = 0
    if n == 9:
        quit()
