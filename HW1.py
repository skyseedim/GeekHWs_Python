""" 1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран. """

a = 'Python'
b = 6.5
c = 5
print(f"\n>> Задание № 1 \nпеременная a = {a},переменная b = {b},переменная c = {c}")
a, b, c = None, None, None
a = input("Введите текст: ")
b = float(input("Введите число с плавающей запятой: "))
c = int(input("Введите целое число: "))
print(f"переменная a = {a},переменная b = {b},переменная c = {c}")
a, b, c = None, None, None

""" 2. Пользователь вводит время в секундах. Переведите время в часы, 
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк. 
"""

t = float(input("\n>> Задание № 2 \nВведите время в секундах: "))
hour = int(t // 3600)
minute = int((t - hour * 3600) // 60)
sec = int(t - hour * 3600 - minute * 60)
print(f"{hour:02}:{minute:02}:{sec:02}")

""" 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, 
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

a = str(int(input("\n>> Задание № 3 \nВведите целое число: ")))
print(f"результат: {int(a) + int(a + a) + int(a + a + a)}")
a = None

""" 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""

a = int(input("\n>> Задание № 4 \nВведите целое число: "))
b = 0
while True:
    c = a % 10
    if c > b:
        b = c
    a = a // 10
    if a == 0:
        break
print(b)
print(f"Самая большая цифра в числе: {b}")
a, b, c = None, None, None

""" 5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, 
вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы 
в расчете на одного сотрудника.
"""

a = float(input("\n>> Задание № 5 \nВыручка фирмы: "))
b = float(input("Издержки фирмы: "))
if a > b:
    print("Отлично, у фирмы прибыль!")
    c = round((a - b) / a, 2)
    print(f"Рентабельность выручки: {c}")
    n = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {round((a - b) / n, 2)}")
elif a < b:
    print("Увы, у фирмы убыток (")
else:
    print("Неплохо, у фирмы нулевая (нормальная) прибыль")
a, b, c, n = None, None, None, None

""" 6. Спортсмен занимается ежедневными пробежками. В первый день его результат 
составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно 
предыдущего. Требуется определить номер дня, на который результат спортсмена составит 
не менее b километров. Программа должна принимать значения параметров a и b и  выводить 
одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат: 
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км. 
"""

a = float(input("\n>> Задание № 6 \nВведите сколько км спортсмен пробежал в первый день: "))
b = float(input("Введите целевой показатель в км: "))
c = a
n = 2
print("Результат:")
print(f"1-й день: {round(a, 2)} км")
while n > 0:
    c = c + 0.1*c
    print(f"{n}-й день: {round(c, 2)} км")
    if c >= b:
        print(f"На {n}-й день спортсмен достигнет результата - не менее {b} км.")
        break
    n += 1
