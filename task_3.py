# 📌 Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.
#---------------------------------------------------------------------
# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.


class BaseExcept(Exception):
    pass


class LevelError(BaseExcept):
    def __str__(self):
        return f'Ошибка уровня доступа. Ввод уровня отсутствует или введен неверный уровень'


class AccessError(BaseExcept):
    def __str__(self):
        return f'Отказ в доступе. Всем постам проверить нарушителя в секторе Д1.'


# try:
#     raise LevelError("Ошибка уровня")
# except LevelError as exp:
#     print(f'Error: {exp}')
#
# try:
#     raise AccessError("Ошибка доступа")
# except AccessError as exp:
#     print(f'Error: {exp}')
