class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} start to go'

    def stop(self):
        return f'{self.name} is stop '

    def turn_right(self):
        return f'{self.name} is turning right'

    def turn_left(self):
        return f'{self.name} is turning left'

    def show_speed(self):
        return f'{self.name} speed is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Town car {self.name} speed is {self.speed}')

        if self.speed > 60:
            print(f'Over speed {self.name}')

    def police(self):
        if self.is_police:
            return f'This car {self.name} from police'
        else:
            return f'This car {self.name} is not from police'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'This car {self.name} from police'
        else:
            return f'This car {self.name} is not from police'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')

        if self.speed > 40:
            return f'{self.name} is over speed '

    def police(self):
        if self.is_police:
            return f'This car {self.name} from police'
        else:
            return f'This car {self.name} is not from police'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'This car {self.name} from police'
        else:
            return f'This car {self.name} is not from police'


merc = TownCar(65, 'white', 'mercedezbenz', False)
maz = WorkCar(70, 'orange', 'MAZ6200', False)
lada = PoliceCar(25, 'black', 'lada-kalina', True)
suzuki = SportCar(110, 'blue', 'suzuki-s4', False)

print(maz.show_speed())
print(lada.is_police)
print(lada.police())
print(f'{merc.color} {merc.name}')
print(f'{suzuki.name} {suzuki.speed} {suzuki.color} {suzuki.police()}')
