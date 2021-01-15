"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, введя переключение цветов в отдельном потоке (С помощью класса Threads)
и реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
Подсказка: Подтверждения переключение можно показать вызовом print(self.color) через заданные
промежутки времени для каждого цвета.
"""

print("Task № 1")
class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'жёлтый', 'зелёный']

#обратный отсчёт
    def __countdown__(self, n):
        self.n = n
        import time, sys
        for i in range(self.n, 0, -1):
            self.__l = ' '
            if i == 1:
                self.__l = '\n'
            sys.stdout.write(str(i) + self.__l)
            sys.stdout.flush()
            time.sleep(1)

#метод переключения сфетофора
    def running(self):
        print(self.__color[0])
        self.__countdown__(7)
        print(self.__color[1])
        self.__countdown__(2)
        print(self.__color[2])
        self.__countdown__(10)

tl = TrafficLight()
tl.running()

# не совсем понял как реализовать решение с Thread, поэтому надеюсь на помощь ) Ниже, что получилось:
from threading import Thread
class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'жёлтый', 'зелёный']
        self.__act_time = [7, 2, 10]

#обратный отсчёт
    def __countdown__(self, n):
        self.n = n
        import time, sys
        for i in range(self.n, 0, -1):
            self.__l = ' '
            if i == 1:
                self.__l = '\n'
            sys.stdout.write(str(i) + self.__l)
            sys.stdout.flush()
            time.sleep(1)

#метод переключения сфетофора
    def running(self, n):
        self.n = n
        print(self.__color[n])

    def run_time(self, t):
        self.t = t
        self.__countdown__(self.__act_time[t])

def proc(fun1, fun2, args1):
    thread_list = []
    t1 = Thread(target=fun1, args=args1)
    thread_list.append(t1)
    t2 = Thread(target=fun2, args=args1)
    thread_list.append(t2)
    return thread_list

tl = TrafficLight()
#while True:
for i in range(3):
    thread_list = proc(tl.running, tl.run_time, (i,))
    print(thread_list)
    for th in thread_list:
        th.start()
        th.join()

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

print("\nTask № 2")
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

#метод рассчёта масс
    def mass(self, rel_mass = 25, thikness = 5):
        self.rel_mass = rel_mass
        self.thikness = thikness
        print(f'при массе асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см = {self.rel_mass} кг \n',\
        f'и толщине равной {self.thikness} см, масса асфальта равна:')
        print(self._length * self._width * self.rel_mass * self.thikness)
rd = Road(20, 5000)
rd.mass()

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода 
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

print("\nTask № 3")
class Worker:
    def __init__(self, name = 'Leo', surname = 'Tolstoy', position = 'writer', wage = 100000, bonus = 800000):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print('Имя, Фамилия: ', self.name, self.surname)
    def get_total_income(self):
        print('доход: ', sum(self._income.values()))

pos = Position()
pos.get_full_name()
pos.get_total_income()
# Проверка работы примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров):
pos = Position('Fyodor', 'Dostoevsky', 'writer', 80000, 700000)
print(pos.name, pos.surname, pos.position)
pos.get_full_name()
pos.get_total_income()

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: 
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать 
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""

print("\nTask № 4")
class Car:
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print('Машина поехала')
        else:
            print('Попытайтесь завести Ваш автомобиль')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')
        else:
            print('Тормози!')

    def turn(self, direction):
        self.direction = direction
        print('Машина повернула ', direction)

    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)

class TownCar(Car):
    def description(self):
        if self.is_police == False:
            print(f'{self.color} {self.name} - Ваш личный автомобиль. Вы едите со скоростью {self.speed}')
        else:
            print('Если Вы не задержаны, покиньте полицейскую машину')

    def show_speed(self):
        print('Ваша скорость: ', self.speed)
        if self.speed > 60:
            print('Вы превышаете скорость!')

class SportCar(Car):
    def description(self):
        if self.is_police == False:
            print(f'{self.color} {self.name} - Ваш спортивный автомобиль. Вы едите со скоростью {self.speed}')
        else:
            print('Если Вы не задержаны, покиньте полицейскую машину')

class PoliceCar(Car):
    def description(self):
        if self.is_police == True:
            print(f'{self.color} {self.name} - Вы полисмен. Вы едите со скоростью {self.speed}')
        else:
            print('Пересядьте в коп-тачку')

class WorkCar(Car):
    def description(self):
        if self.is_police == False:
            print(f'{self.color} {self.name} - Ваш рабочий автомобиль. Вы едите со скоростью {self.speed}')
        else:
            print('Если Вы не задержаны, покиньте полицейскую машину')

    def show_speed(self):
        print('Ваша скорость: ', self.speed)
        if self.speed > 40:
            print('Вы превышаете скорость!')

pos = WorkCar(90, 'red', 'Tesla', False)
pos.description()
pos.show_speed()
print()
pos = SportCar(0, 'green', 'Lada', True)
pos.description()
pos.go()
pos.turn('на право')
pos.stop()

"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) 
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, 
что выведет описанный метод для каждого экземпляра.
"""

print("\nTask № 5")
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} - это ручка, я пишу!')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} - это карандаш, меня можно стереть!')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} - это маркер, и я выделяю!')

p = Pen('SuperPen')
p.draw()

pn = Pencil('SuperPencil')
pn.draw()

h = Handle('SuperHandle')
h.draw()
