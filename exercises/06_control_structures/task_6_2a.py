# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')
#list_ip_address = ip_address.split(".")
first_octet = ip_address.split(".")[0]

if len(ip_address.split(".")) != 4:
    print("Неправильный IP-адрес")
elif (ip_address.split(".")[0].isdigit() and ip_address.split(".")[1].isdigit() and ip_address.split(".")[2].isdigit() and ip_address.split(".")[3].isdigit()) == False:
   print("Неправильный IP-адрес")
elif ((0 <= int(ip_address.split(".")[0]) <= 255) and (0 <= int(ip_address.split(".")[1]) <= 255) and (0 <= int(ip_address.split(".")[2]) <= 255) and (0 <= int(ip_address.split(".")[3]) <= 255)) == False:
   print("Неправильный IP-адрес")
else:
   if 1 <= int(first_octet) <= 223:
      print('unicast')
   elif 224 <= int(first_octet) <= 239:
      print('multicast')
   elif ip_address == '255.255.255.255':
      print('local broadcast')
   elif ip_address == '0.0.0.0':
      print('unassigned')
   else:
      print('unused')
