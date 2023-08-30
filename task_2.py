# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.

def get_value(diction: dict, key, value_default=None):
    try:
        spam = diction[key]
    except KeyError as exp:
        spam = value_default

    return spam


if __name__ == '__main__':
    dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_value(dict, 'a'))
    print(get_value(dict, 'd'))
