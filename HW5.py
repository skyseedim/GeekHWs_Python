"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

print("Task № 1")
out_f = open("out_file.txt", "w")
my_list = []
while True:
    string = input("Введите данные (Для завершения оставьте строку пустой): ")
    if len(string) == 0:
        print("Ввод данных завершён")
        break
    my_list.append(string + '\n')
out_f.writelines(my_list)
out_f.close()

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

print("\nTask № 2")
with open("Task_2_text.txt") as f_obj:
    cont = f_obj.readlines()
res = []
res.extend([(i+1, len(string.split())) for i, string in enumerate(cont)])
print(res)
print(f" Количество строк в файле: {len(cont)}")
for data in res:
    print(f" Количество слов в {data[0]}-й строке: {data[1]}")

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

print("\nTask № 3")
with open("Task_3_text.txt") as f_obj:
    cont = f_obj.readlines()

res = []
res.extend([(string.split()[0], float(string.split()[1])) for string in cont])
print(res)
print(f"Фамилии сотруднико с окладом менее 20000:")
for data in res:
    if data[1] < 20000:
        print(data[0])

# print([data[0]) for data in res if data[1] < 20000])
import statistics as stat
print("Средние величин дохода сотрудников:")
my_list = []
my_list.extend([data[1] for data in res])
print(" - арифметическое: ", stat.fmean(my_list))
print(" - медиана: ", stat.median(my_list))
print(" - мода: ", stat.mode(my_list))

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

print("\nTask № 4")
with open("Task_4_text_1.txt") as f_obj:
    cont = f_obj.readlines()

res = []
res.extend([[string.split("-")[0].rstrip(), string.split("-")[1]] for string in cont])
res[0][0] = "Один -"
res[1][0] = "Два -"
res[2][0] = "Три -"
res[3][0] = "Четыре -"
with open("Task_4_text_2.txt", "w") as f_obj:
    [f_obj.writelines(string) for string in res]

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

print("\nTask № 5")
my_list = None
import random
my_list = random.sample(range(0,1000000), 10)
with open("Task_5_text.txt", "w") as f_obj:
    [f_obj.write(str(num) + ' ') for num in my_list]

with open("Task_5_text.txt") as f_obj:
    cont = f_obj.read()
my_list = []
my_list.extend([float(num) for num in cont.split()])

print("Сумма чисел в файле: ", sum(my_list))

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет 
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

print("\nTask № 6")
with open("Task_6_text.txt") as f_obj:
    cont = f_obj.readlines()
# переводим данные из файла в словарь (убираем уточнения в скобках, но с прочерками)
my_dict = {les.split(":")[0]: [num.split("(")[0] for num in les.split(":")[1].split()] for les in cont}
# формируем требуемый словарь, в т.ч. подсчитываем общее кол-во занятий и игнорируем прочерки
res = {}
for key in my_dict.keys():
    my_list_temp = []
    for num in my_dict[key]:
        try:
            my_list_temp.append(int(num))
        except:
            continue
    res[key] = sum(my_list_temp)
print('Cловарь, содержащий название предмета и общее количество занятий по нему: \n', res)

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь 
(со значением убытков).
Пример списка: 
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

print("\nTask № 7")
with open("Task_7_text.txt") as f_obj:
    cont = f_obj.readlines()
# переводим данные из файла в словарь - название фирмы (ключ) и рассчитанная прибыль или убыток
my_dict = {les.split()[0]: float(les.split()[2]) - float(les.split()[3]) for les in cont}
# формируем список со значениями прибылей
prof_list = []
for prof in my_dict.values():
    if prof >= 0:
        prof_list.append(prof)
# формируем итоговый список из словаря с данными и нового словаря с рассчитанной средней прибылью
res_list = [my_dict, {"average_profit": round(stat.fmean(prof_list),2)}]
print("Итоговый список, содержащий словарь с фирмами и их прибылями, а также словарь со средней прибылью: \n", res_list)
import json
with open("profit.json", "w") as write_f:
    json.dump(res_list, write_f)
