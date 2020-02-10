class Road:
    __length = None
    __width = None
    weight = None
    thickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road_to_village object')

    def mass(self):
        self.weigth = 30
        self.thickness = 0.08
        mass = self.length * self.width * self.weigth * self.thickness / 1000
        print(f'Need {mass} ton for the building')

road_to_village = Road(20000, 6)
road_to_village.mass()