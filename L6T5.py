class Stationery:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f'Запуск отрисовки {self.name}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск письма {self.name}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск черчения {self.name}')

class Marker(Stationery):
    def draw(self):
        print(f'Запуск рисования {self.name}')

draw = Stationery('красками')
draw.draw()

pen = Pen('ручкой')
pen.draw()

pencil = Pencil('карандашом')
pencil.draw()

marker = Marker('маркером')
marker.draw()
