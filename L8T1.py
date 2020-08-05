class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_str(self):
        return self.str_conversion(self.day, self.month, self.year)

    @classmethod
    def str_conversion(cls, str_1, str_2, str_3):
        int_1 = int(str_1)
        int_2 = int(str_2)
        int_3 = int(str_3)
        return int_1, int_2, int_3

    @staticmethod
    def date_validation(self):
        if self[0] <= 0 or self[1] <= 0 or self[2] <= 0:
            print('Date can\'t equal 0 or be negative!')
            quit()
        if self[0] > 31:
            print('There can\'t be more than 31 days in a month! ')
            quit()
        if self[1] > 12:
            print('There can\'t be more than 12 months in a year! ')
            quit()
        else:
            print('-'.join("{:02}".format(v) for v in self))


date = Date('23', '05', '2020')
Date.date_validation(date.get_str())
