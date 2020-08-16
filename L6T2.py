class Road:
    def __init__(self, width, length, thickness):
        self._width = width
        self._length = length
        self._thickness = thickness

    def asphalt_mass(self):
        mass = self._length * self._width * 25 * self._thickness
        print(f'{self._width}m * {self._length}m * 25kg * {self._thickness}cm = {mass / 1000}t')

width = float(input('Enter width of the road: '))
length = float(input('Enter length of the road: '))
thickness = float(input('Enter thickness of the road: '))

road_calc = Road(width, length, thickness)
road_calc.asphalt_mass()
