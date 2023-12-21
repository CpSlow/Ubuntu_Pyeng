# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

list_of_list = []
vlan_number = input('Enter VLAN number: ')
result = []

with open('CAM_table.txt') as file:
    for line in file:
        line_list = line.split()
        if ((len(line_list) > 0) and (line_list[0].isdigit())):
            sorted_list = [line_list[0], line_list[1], line_list[3]]
            list_of_list.append(sorted_list)

for i in range(len(list_of_list)):
    list_of_list[i][0] = int(list_of_list[i][0])

for i in range(len(list_of_list)):
    if list_of_list[i][0] == int(vlan_number):
        result.append(list_of_list[i])

for i in range(len(result)):
   print("{:<10} {:>10} {:>10}".format(result[i][0], result[i][1], result[i][2]))