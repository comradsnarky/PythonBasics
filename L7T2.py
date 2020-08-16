class Clothes:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        total_cloth = self.__dict__.get('cloth_coat') + other.__dict__.get('cloth_suit')
        return print(f'Total cloth length for both items is {total_cloth.__round__(2)}m')

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_cloth(self):
        cloth_coat = self.size / 6.5 + 0.5
        self.cloth_coat = cloth_coat
        return self.name, self.cloth_coat.__round__(2)

class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def get_cloth(self):
        cloth_suit = 2 * self.height + 0.3
        self.cloth_suit = cloth_suit
        return self.name, self.cloth_suit.__round__(2)

coat = Coat('Coat', 10)
print(f'Cloth length for {coat.get_cloth()[0]} is {coat.get_cloth()[1]}m')

suit = Suit('Suit', 1.8)
print(f'Cloth length for {suit.get_cloth()[0]} is {suit.get_cloth()[1]}m')

coat + suit
