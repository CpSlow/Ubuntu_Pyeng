# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
new_config = ""
from sys import argv
config = argv[1]
new_file = argv[2]

from sys import argv
config = argv[1]

with open(config, 'r') as f:
    for line in f:
        if line[0] != '!' and not(ignore[0] in line) and not(ignore[1] in line) and not(ignore[2] in line):
           #print(line.rstrip())
            new_config += line

with open(new_file, 'w') as file:
    file.write(new_config)
