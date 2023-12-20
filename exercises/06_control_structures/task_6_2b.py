# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')
#list_ip_address = ip_address.split(".")
correct_ip = False

while not correct_ip:
    if len(ip_address.split(".")) != 4:
        print("Неправильный IP-адрес")
        ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')
    elif (ip_address.split(".")[0].isdigit() and ip_address.split(".")[1].isdigit() and ip_address.split(".")[2].isdigit() and ip_address.split(".")[3].isdigit()) == False:
        print("Неправильный IP-адрес")
        ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')
    elif ((0 <= int(ip_address.split(".")[0]) <= 255) and (0 <= int(ip_address.split(".")[1]) <= 255) and (0 <= int(ip_address.split(".")[2]) <= 255) and (0 <= int(ip_address.split(".")[3]) <= 255)) == False:
        print("Неправильный IP-адрес")
        ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')
    else:
        if 1 <= int(ip_address.split(".")[0]) <= 223:
            print('unicast')
        elif 224 <= int(ip_address.split(".")[0]) <= 239:
            print('multicast')
        elif ip_address == '255.255.255.255':
            print('local broadcast')
        elif ip_address == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
        correct_ip = True
