
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engile_power,):
        self.owner = owner
        self.__model = __model
        self.__engile_power = __engile_power
        self.__color = __color
    def get_model(self):
        return  f'Модель :{self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя : {self.__engile_power}'
    def get_color(self):
        return f'Цвет : {self.__color}'
    def print_info (self):
        print(Vehicle.get_model(self))
        print(Vehicle.get_horsepower(self))
        print(Vehicle.get_color(self))
        print(f'Владелец : {self.owner}')

    def set_color(self, new_color):
        for i in Vehicle.__COLOR_VARIANTS:
            if new_color.lower() in i.lower():
                self.__color = new_color
                break
        else:
            print(f'Нельльзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
