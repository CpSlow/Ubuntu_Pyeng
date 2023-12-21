# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = {}
param = []

with open('ospf.txt') as o:
    for line in o:
        line_list = line.split() 
        param.append(line_list[1])
        param.append(line_list[2].strip('[]'))
        param.append(line_list[4].strip(','))
        param.append(line_list[5].strip(','))
        param.append(line_list[6])
        print()
        print("Prefix                {}".format(param[0]))
        print("AD/Metric             {}".format(param[1]))
        print("Next-Hop              {}".format(param[2]))
        print("Last update           {}".format(param[3]))
        print("Outbound Interface    {}".format(param[4]))
        param = []