import time


#1
# class TrafficLight:
#     color = ''
#
#     def running(self):
#         self.color = ['Красный', 'Желтый', 'Зеленый']
#         print(self.color[0])
#         time.sleep(7)
#         print(self.color[1])
#         time.sleep(2)
#         print(self.color[2])
#         time.sleep(4)
#
# TrafficLight().running()

#2
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def mass_calculation(self, mass_asphalt, road_thickness):
#         print(f'Required asphalt for 1 sq.m of road - '
#               f'{(self._length * self._width * mass_asphalt * road_thickness) / 1000} tons.')
#
# a = Road(20, 5000).mass_calculation(25, 5)

#3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': wage, 'bonus': bonus}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f'Имя сотрудника: {self.surname} {self.name}'
#
#     def get_total_income(self):
#         return (f'Общий доход сотрудника состовляет: '
#                 f'{self._income["wage"] + self._income["bonus"]} рублей')
#
# a = Position(name='Иван', surname='Сидоров', position='Столяр', wage=20000, bonus=5000)
# print(f'Атрибуты класса: {a.name}, {a.surname}, {a.position}, {a._income}')
# print(a.get_full_name())
# print(f'Должность сотрудника: {a.position}')
# print(a.get_total_income())

#4
# class Car:
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return 'Машина поехала'
#
#     def stop(self):
#         return 'Машина остановилась'
#
#     def turn(self, direction):
#         return f'Машина повернула {direction}'
#
#     def show_speed(self):
#         return f'Скорость автомобиля: {self.speed}'
#
#     def __str__(self):
#         return (f'Данные об автомобиле\n'
#                 f'Марка: {self.name}, Цвет: {self.color}, Это полиция: {self.is_police}')
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             return f'Вы превысили скорость. Ваша скорость {self.speed} км/ч'
#         else:
#             return f'Ваша скорость {self.speed}'
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             return f'Вы превысили скорость. Ваша скорость {self.speed} км/ч'
#         else:
#             return f'Ваша скорость {self.speed}'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police=True):
#         super().__init__(speed, color, name, is_police)
#
# a = PoliceCar(70, 'white', 'Logan')
# print(a)

#5
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return 'Запуск отрисовки.'
#
#
# class Pen(Stationery):
#     def draw(self):
#         return f'Рисуем ручкой: {self.title}'
#
#
# class Pencil(Stationery):
#     def draw(self):
#         return f'Рисуем карандашом: {self.title}'
#
# class Handle(Stationery):
#     def draw(self):
#         return f'Рисуем маркером: {self.title}'
#
# a = Pen('Что-нибудь!')
# print(a.draw())