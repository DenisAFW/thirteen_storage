# 📌 Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

def input_num() -> float:
    while True:
        try:
            spam = float(input('Введите целое или вещественное число: '))

        except ValueError as ve:
            print(f"Введены неверные данные! - {ve}")
        else:
            return spam


if __name__ == '__main__':
    print(input_num())
