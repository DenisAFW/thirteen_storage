# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня доступа.
from task_3 import LevelError
from task_3 import AccessError
import json


class UserWorkshop:

    def __init__(self, name, p_id, level):
        self.name = name
        self.id = p_id
        self.level = level

    def __str__(self):
        return f'name: {self.name}, id: {self.id}, level: {self.level}'


def load_users(path: str = 'test_bd.json'):
    spam = input('Введите имя и уровень доступа через пробел:\n')

    try:
        data = spam.split()
        input_name = data[0]
        input_key = data[1]
    except IndexError as exp:
        print(f'Введены неверные данные -> {exp}')
    keys = []
    names = []
    keys_count, names_count = 0, 0

    try:
        with open(path, 'r', encoding='utf-8') as fj:
            user_dict = json.load(fj)
        for level, user_list in user_dict.items():
            for p_id, name in user_list.items():
                keys.append(p_id)
                names.append(name)
        try:
            if input_name in names:
                for i in names:
                    if input_name != i:
                        names_count += 1
                    else:
                        break
            else:
                raise AccessError
        except UnboundLocalError as exp:
            print(f'Не введено имя пользователя!-> {exp}')
        try:
            if input_key in keys:
                for i in keys:
                    if input_key != i:
                        keys_count += 1
                    else:
                        break
            else:
                raise LevelError
        except UnboundLocalError as exp:
            print(f'Не введен уровень доступа! -> {exp}')

        if keys[keys_count] == input_key and names[names_count] == input_name:
            print('Добро пожаловать домой, Агент К')
        else:
            raise AccessError

    except FileNotFoundError as exp:
        print(f'File no found -> {exp}')


if __name__ == '__main__':
    load_users()
