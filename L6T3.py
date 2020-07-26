class Worker:
    def __init__(self, name, l_name, position, hours):
        self.name = name
        self.l_name = l_name
        self.position = position
        self.hours = hours

class Position(Worker):
    def get_full_name(self):
        employee_dict['name'] = (f'{self.name} {self.l_name}').title()
        employee_dict['position'] = self.position.title()
        employee_dict['hours'] = self.hours

    def get_total_income(self):
        wage = {'bus driver': [2000.46, 1.3], 'cashier': [1500.79, 1.2], 'technician': [2000.13, 1.5]}
        for i in wage.keys():
            if self.position == i:
                wage_list = wage.get(i)
                income = self.hours * wage_list[0] * wage_list[1]
                self.__income = income.__round__(2)
        employee_dict['income'] = self.__income

employee_dict = {'name': '', 'position': '', 'hours': '', 'income': ''}

name = input('Enter employee\'s name: ')
l_name = input('Enter employee\'s last name: ')
position = input('Enter employee\'s position: ').lower()
hours = float(input('Enter the number of hours worked: '))

employee = Position(name, l_name, position, hours)
employee.get_full_name()
employee.get_total_income()
print(employee_dict)

with open('L6T3.txt', 'a', encoding='utf-8') as my_f:
    my_f.write('\n')
    for i, k in employee_dict.items():
        my_f.write(f'{i}: {k}\n')
my_f.close()
