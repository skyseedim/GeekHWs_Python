"""
1. 1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
на реальных данных.
"""

print("Task № 1")
class Date:
    def __init__(self, dt):
        Date.dt = dt

    @classmethod
    def date_number(cls):
        return cls.dt.split('-')[0]

    @staticmethod
    def is_valid(dt):
        num_list = dt.split('-')
        num_dict = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
        if int(num_list[2]) < 1900 or int(num_list[2]) > 2021:
            print('Введите корректный год!')
        elif int(num_list[1]) < 1 or int(num_list[1]) > 12:
            print('Введите корректный месяц!')
        elif int(num_list[0]) < 1 or int(num_list[0]) > num_dict[num_list[1]]:
            print('Введите корректное число!')
        else:
            print('Всё корректно!')

Date.is_valid('10-01-2021')
Date.is_valid('10-01-256549161')
Date.is_valid('31-02-2020')
Date.is_valid('31-13-2020')

num = Date('28-02-1905')
print('Число: ', num.date_number())

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, 
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию 
и не завершиться с ошибкой.
"""

print("\nTask № 2")
class Error(Exception):
    def __init__(self, message="Деление на ноль!"):
        self.message = message

    def __str__(self):
        return self.message

def div_er():
    list_of_num = input("Введите два числа через пробел, которые нужно поделить: ").split()
    try:
        if float(list_of_num[1]) == 0:
            raise Error()
        else:
            print('результат деления ', float(list_of_num[0]) / float(list_of_num[1]))
    except Error as err:
        print(err)

div_er()
div_er()

"""
3.	Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо 
только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится 
на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем 
очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.
"""

print("\nTask № 3")
class Error2(Exception):
    def __init__(self, number=None, message="Введите число, а не строку!"):
        Error2.message = message
        Error2.num = number

    @classmethod
    def is_num(cls):
        try:
            return float(cls.num)
        except ValueError:
            print(cls.message)
            return '!'

def num_list():
    res_list = []
    while True:
        data = input("Введите число (для завершения введите stop): ")
        if data == 'stop':
            print(res_list)
            break
        else:
            numb_cl = Error2(number=data)
            numb = numb_cl.is_num()
            if numb != '!':
                res_list.append(numb)

num_list()

"""
4.	Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите 
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, 
уникальные для каждого типа оргтехники.
5.	Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём 
оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую 
подходящую структуру (например, словарь).
6.	Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем 
данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать 
строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП.
"""

print("\nTasks №№ 4-6")
import datetime
import json
import random

class Error3(Exception):
    def __init__(self, message="На складе не хватает оборудования для передачи в подразделение!"):
        Error3.message = message


class OfficeStorage:
    def __init__(self, eq_dict={}, new_eq_dict={}):
        self.__stor_eq = eq_dict
        self.__new_eq_dict = new_eq_dict

    #Метод поступления техники на склад. Возвращает словарь и записывает его в json файл
    def new_eq(self):
        for eq_type, par in self.__new_eq_dict.items():
            dt_now = str(datetime.datetime.now().timestamp())
            #dt_now (текущее время в сек с 1970) нужен для id процедуры поступления/передачи оборудования
            # Формат id: P/S/C_'dt_now'.'случайное число от 1 до 1000000
            try:
                self.__stor_eq[eq_type].update({eq_type[:1] + '_' + dt_now + '.' + str(random.randint(1, 1000000)): [par, 'Storage']})
                print(f"Ещё одно оборудование {eq_type} поступило на склад")
            except KeyError:
                self.__stor_eq[eq_type] = {eq_type[:1] + '_' + dt_now: [par, 'Storage']}
                print(f"Новое оборудование {eq_type} поступило на склад")

            with open("Office_Equipment.json", "w") as write_f:
                json.dump(self.__stor_eq, write_f)
            return self.__stor_eq

    # Метод передачи техники в подразделения. Возвращает словарь и записывает его в json файл
    def eq_transfer(self, division, id_num, num_transfer):
        self.division = division
        self.__id_num = id_num #id процедуры (см.выше в new_eq)

        # проверка того, что num_transfer (число оборудования отпровляемые в подразделения) - это число. Если нет,
        # то предлагает ввести правильное значение без выхода из скрипта. Воспользовался классом Error2 из задания 3.
        while True:
            numb_cl = Error2(number=num_transfer)
            numb = numb_cl.is_num()
            if numb != '!':
                self.num_transfer = int(numb)
                break
            else:
                num_transfer = input(f"Введите количество оборудования для отправки в подразделение {self.division}: ")

        if id_num[:1] == 'P': #id поможет определить тип оборудования
            stor_key = 'Printer'
        elif id_num[:1] == 'S':
            stor_key = 'Scanner'
        elif id_num[:1] == 'C':
            stor_key = 'Copier'
        num_in_stor = self.__stor_eq[stor_key][self.__id_num][0][0] #число оборудования на складе

        while True: # нужен только для обработки ситуации, когда количество передоваемых устройств меньше хранящихся на складе
            if num_in_stor == self.num_transfer:
                self.__stor_eq[stor_key][self.__id_num][1] = self.division
                print(f"Всё оборудование передано в подразделение {self.division}")
                break
            elif num_in_stor > self.num_transfer:
                dt_now = str(datetime.datetime.now().timestamp())
                self.__stor_eq[stor_key][self.__id_num][0][0] -= self.num_transfer
                self.__stor_eq[stor_key].update({stor_key[:1] + '_' + dt_now: [
                    [self.num_transfer] + self.__stor_eq[stor_key][self.__id_num][0][1:], self.division]})
                print(f"Часть оборудования передано в подразделение {self.division}")
                break
            else:  #Если число оборудования для отправки меньше хранящегося на складе, то выходит ошибка и предложение поменять его
                try:
                    raise Error3()
                except Error3 as err:
                    print(err)
                    self.num_transfer = int(input(f"На складе осталось {num_in_stor} шт. оборудования.\n Введите корректное количество \
оборудования для отправки в подразделение {self.division} (Для выхода введите нечисловой символ): "))

        with open("Office_Equipment.json", "w") as write_f:
            json.dump(self.__stor_eq, write_f)
        return self.__stor_eq


class OfficeEq:
    def __init__(self, num, date, brand, model, pap_form='A4'):
        self.num = num
        self.date = date
        self.brand = brand
        self.model = model
        self.pap_form = pap_form

class Printer(OfficeEq):
    def __init__(self, num, date, brand, model, pap_in_min, pap_form='A4', type='Laser', \
                 two_side_print=False, color=False):
        super().__init__(num, date, brand, model, pap_form)
        self.color = color
        self.two_side_print = two_side_print
        self.type = type
        self.pap_min = pap_in_min

    def new_printer(self):
        print("Новый принтер")
        return {'Printer': [self.num, self.date, self.brand, self.model, self.pap_form, self.type, \
                            self.pap_min, self.color, self.two_side_print]}

class Scanner(OfficeEq):
    def __init__(self, num, date, brand, model, dpi, pap_form='A4'):
        super().__init__(num, date, brand, model, pap_form)
        self.dpi = dpi

    def new_scan(self):
        print("Новый сканер")
        return {'Scanner': [self.num, self.date, self.brand, self.model, self.pap_form, self.dpi]}

class Copier(OfficeEq):
    def __init__(self, num, date, brand, model, dpi, pap_form='A3', two_side_copy=False, two_side_print=False):
        super().__init__(num, date, brand, model, pap_form)
        self.dpi = dpi
        self.two_side_copy = two_side_copy
        self.two_side_print = two_side_print

    def new_copier(self):
        print("Новый ксерокс")
        return {'Copier': [self.num, self.date, self.brand, self.model, self.pap_form, self.dpi. \
            self.two_side_copy, self.two_side_print]}


pr1 = Printer(num=10, date='10-02-2020', brand='HP', model='LP56', pap_in_min=30)
print(pr1.new_printer())
o_str = OfficeStorage(new_eq_dict=pr1.new_printer())
dict11 = o_str.new_eq()
print(dict11)
pr2 = Printer(num=2, date='20-02-2020', brand='Kyocera', model='FS1255', pap_in_min=40)
print(pr2.new_printer())
o_str2 = OfficeStorage(eq_dict=dict11, new_eq_dict=pr2.new_printer())
dict12 = o_str2.new_eq()
print(dict12)
print('Из сохраненного файла')
with open("Office_Equipment.json") as read_f:
    data = json.load(read_f)
print(data)
print('--------------------------------------------------------------------------------')
o_str3 = OfficeStorage(eq_dict=dict12)
dict21 = o_str3.eq_transfer(division='OK', id_num=list(data['Printer'].keys())[0], num_transfer=4)
print(dict21)
o_str4 = OfficeStorage(eq_dict=dict21)
dict22 = o_str3.eq_transfer(division='OOiR', id_num=list(data['Printer'].keys())[1], num_transfer=2)
print(dict22)
print('Из сохраненного файла')
with open("Office_Equipment.json") as read_f:
    data2 = json.load(read_f)
print(data2)
print('--------------------------------------------------------------------------------')
o_str5 = OfficeStorage(eq_dict=data2)
dict31 = o_str3.eq_transfer(division='CAG', id_num=list(data['Printer'].keys())[0], num_transfer='str')
print(dict31)

"""
7.	Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса 
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного 
результата.
"""
print("\nTask № 7")
class Complex:
    def __init__(self, compl_numb=(1, 1)):
        self.real_part = compl_numb[0]
        self.im_part = compl_numb[1]

    def __add__(self, other):
        return (self.real_part + other.real_part, self.im_part + other.im_part)

    def __mul__(self, other):
        return(self.real_part * other.real_part - self.im_part * other.im_part, self.real_part * other.im_part + \
               other.real_part * self.im_part)

    def __str__(self):
        return str(self.real_part) + ' + ' + str(self.im_part) + 'i'


cnum1 = Complex((5, 6))
cnum2 = Complex((3, 4))
csum = cnum1 + cnum2
print(Complex(csum))
cmul = cnum1 * cnum2
print(Complex(cmul))
print(cnum1)






























