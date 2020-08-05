class Stock:
    def __init__(self, *args):
        self.args = args[0]

    def in_stock(self, stock_dict):
        self.stock_dict = stock_dict
        if self.args[0] in self.stock_dict.keys():
            self.stock_dict.get(self.args[0]).append(self.args[1:6])
        else:
            self.stock_dict.update({self.args[0]: [self.args[1:6]]})
        return self.stock_dict

    def out_stock(self, key, value, quantity):
        self.stock_dict = self.__dict__.get('stock_dict')
        self.key = key
        self.value = value
        self.quantity = quantity
        for k in self.stock_dict.keys():
            if self.key == k:
                for el in self.stock_dict.get(k):
                    if self.value == el:
                        index = self.stock_dict.get(k).index(el)
                        self.stock_dict.get(k)[index][3] = int(self.stock_dict.get(k)[index][3]) - self.quantity
        return self.stock_dict

class OfficeMachinery:
    def __init__(self, name, manufacturer, model, price, quantity):
        self.name = name
        self.mnf = manufacturer
        self.model = model
        self.price = price
        self.quantity = quantity

class Laptop(OfficeMachinery):
    def __init__(self, name, manufacturer, model, price, quantity, productivity_benchmark):
        super().__init__(name, manufacturer, model, price, quantity)
        self.p_b = productivity_benchmark

    def consolidate(self):
        laptop = []
        for k in self.__dict__.keys():
            laptop.append(self.__dict__.get(k))
        return laptop

class Copier(OfficeMachinery):
    def __init__(self, name, manufacturer, model, price, quantity, speed):
        super().__init__(name, manufacturer, model, price, quantity)
        self.speed = speed

    def consolidate(self):
        copier = []
        for k in self.__dict__.keys():
            copier.append(self.__dict__.get(k))
        return copier

class Phone(OfficeMachinery):
    def __init__(self, name, manufacturer, model, price, quantity, kind):
        super().__init__(name, manufacturer, model, price, quantity)
        self.kind = kind

    def consolidate(self):
        phone = []
        for k in self.__dict__.keys():
            phone.append(self.__dict__.get(k))
        return phone

stock_dict = {}
prod_1 = Laptop('Laptop', 'Apple', 'MacBook Pro', 2400, 10, 'Geekbench score - 2997')
prod_2 = Copier('Copier', 'HPE', 'LJ-100', 1000, 5, '30 pages per minute')
prod_3 = Phone('Phone', 'Cisco', 'TR9875', 768, 7, 'VoIP')
prod_4 = Laptop('Laptop', 'Apple', 'MacBook Air', 1300, 6, 'Geekbench score - 2597')
prod_5 = Copier('Copier', 'Epson', 'LT450', 500, 3, '60 pages per minute')
prod_6 = Phone('Phone', 'Siemens', 'S98T', 200, 7, 'Landline')

stock_1 = Stock(prod_1.consolidate())
stock_2 = Stock(prod_2.consolidate())
stock_3 = Stock(prod_3.consolidate())
stock_4 = Stock(prod_4.consolidate())
stock_5 = Stock(prod_5.consolidate())
stock_6 = Stock(prod_6.consolidate())

stock_1.in_stock(stock_dict)
stock_2.in_stock(stock_dict)
stock_3.in_stock(stock_dict)
stock_4.in_stock(stock_dict)
stock_5.in_stock(stock_dict)
stock_6.in_stock(stock_dict)

print(stock_dict)

Stock.out_stock(stock_6, 'Laptop', ['Apple', 'MacBook Air', 1300, 6, 'Geekbench score - 2597'], 2)
Stock.out_stock(stock_6, 'Phone', ['Cisco', 'TR9875', 768, 7, 'VoIP'], 5)

print()
print(stock_dict)
