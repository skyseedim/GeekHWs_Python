"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

print("Task № 1")
my_list = [7, 'format', [3.29, 6.51, 7], None, (31, 12, 54), {'a', 'б', 'в'}, {'key_1': [1, 2], 5: [10, 12]}, True,
           False, ]
for my_list_object in my_list:
    print(f'{my_list_object} - это тип {type(my_list_object)}')
my_list = None

"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""

print("\nTask № 2")
my_input = input("Введите элементы списка, разделяя их тире, например, 1-2-[string1, string2]-6: ")
my_list = list(my_input.split('-'))
for n in range(1, len(my_list), 2):
    my_list[n], my_list[n-1] = my_list[n-1], my_list[n]
print(my_list)
my_input, my_list = None, None

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится 
месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

print("\nTask № 3")
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))

dict_month = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for key, value in dict_month.items():
    if value.count(month) == 1:
        print('Время года: ', key)

list_season = ["Зима", "Весна", "Лето", "Осень", "Зима"]
print('Время года: ', list_season[month // 3])

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

print("\nTask № 4")
my_input = input("Введите строку из нескольких слов, разделённых пробелами: ")
my_list = my_input.split()
for num, word in enumerate(my_list):
    print(num+1, word[:10])
my_input, my_list = None, None

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы 
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

print("\nTask № 5")
my_list = [7, 5, 3, 3, 2]
num = int(input("Введите новый элемент рейтинга: "))
my_list.append(-1)
for n in range(len(my_list)):
    if num > my_list[n]:
        my_list.insert(n, num)
        break
my_list.remove(-1)
print(my_list)

"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — 
номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

#Комментарий: так как работа с файлами ещё не изучена, данные запрашиваю с помощью input
print("\nTask № 6")
amount = int(input("Введите число товаров (позиций): "))
prod_structure = []
for i in range(amount):
	data_input = input(f"Введите название {i+1}-го товара, его цену, количество в шт. через пробел \
	\n(если количество товара измеряется не в штуках, то добавьте через пробел ещё и единицу измерения):\n")
	prod_list = data_input.split()
	if len(prod_list) == 3:
		prod_list.append("шт.")
	elif len(prod_list) <3 or len(prod_list) > 4:
		print("wrong input")
		break
	temp_dict = {"название": prod_list[0], "цена": float(prod_list[1]), "количество": float(prod_list[2]), "ед.": prod_list[3]}
	prod_structure.append((i+1, temp_dict))
	temp_dict = None

list_names = ["название", "цена", "количество", "ед."]
prod_name = [[] for i in range(len(list_names))]
for i in range(len(prod_structure)):
    for j in range(len(list_names)):
	    prod_name[j].extend([prod_structure[i][1][list_names[j]]])
prod_dict = {"название": prod_name[0], "цена": prod_name[1], "количество": prod_name[2], "ед.": prod_name[3]}

print ('структура данных "Товары": ', prod_structure)
print('аналитика о товарах :', prod_dict)
