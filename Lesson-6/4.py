class Car:
    #атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    #методы
    def go(self):
        return f'{self.name} is started'
    def stop(self):
        return f'{self.name} is stopped'
    def turn_right(self):
        return f'{self.name} is turned right'
    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed of work car {self.name} is {self.speed}")

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'
        else:
            return f'Speed of {self.name} is normal for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

bmw = SportCar(100, 'Black', 'BMW', False)
opel = TownCar(30, 'White', 'Opel', False)
mazda = WorkCar(70, 'Grey', 'Mazda', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(mazda.turn_left())
print(f'When {opel.turn_right()}, then {bmw.stop()}')
print(f'{opel.go()} with speed exactly {opel.show_speed()}')
print(f'{mazda.name} is {mazda.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {ford.name}  a police car? {ford.is_police}')
print(bmw.show_speed())
print(opel.show_speed())
print(ford.show_speed())