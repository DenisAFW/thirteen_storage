# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
# -------------------------------------------------------------------------
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv


# my_dict = {'1': 'Alexa',
#            '2': 'Rick',
#            '3': 'Morty'}

# with open('test.pickle', 'wb') as pic_f:
#     pickle.dump(my_dict, pic_f)
def to_csv(file_name):
    try:
        with (open(file_name, 'w', newline='') as csv_f, open('test.pickle', 'rb') as pic_r):
            pic_read = pickle.load(pic_r)
            pic_read = [pic_read]
            keys = pic_read[0].keys()
            dict_writer = csv.DictWriter(csv_f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(pic_read)
    except FileNotFoundError as exp:
        print(f'Файл не найден -> {exp}')


if __name__ == '__main__':
    to_csv('test.csv')
# ---------------------------------------------------------------------------------------------------
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата
try:
    number = int(input('Введите число '))
except ValueError as exp:
    print(f'Введен неверный формат данных -> {exp}')

change = format(number, '#x')
print(change)
if hex(number) == change:
    print('1')
else:
    print('0')
# ---------------------------------------------------------------------------------------------------
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import choices
try:
    count = int(input('Введите длину списка '))
except ValueError as exp:
    print(f'Введен неверный формат данных -> {exp}')
list_nums = choices(range(1, count * 2), k=count)

print(list_nums)

result_list = set()
for i in list_nums:
    if list_nums.count(i) > 1:
        result_list.add(i)

print(result_list)