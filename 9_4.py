from random import choice  # Импортируем функцию choice для случайного выбора

# Часть 1: Lambda-функция для проверки совпадения букв в строках
# Исходные строки
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Используем lambda-функцию для посимвольного сравнения двух строк
# map применяет lambda-функцию к соответствующим элементам двух строк
result = list(map(lambda x, y: x == y, first, second))

# Вывод результата
print(result)
# Ожидаемый результат: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Часть 2: Замыкание для записи данных в файл
def get_advanced_writer(file_name):
    """
    Функция возвращает вложенную функцию для записи данных в файл.
    :param file_name: Имя файла для записи данных.
    """
    def write_everything(*data_set):
        """
        Вложенная функция, которая записывает все переданные данные в файл.
        :param data_set: Неограниченное количество данных для записи.
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')  # Преобразуем данные в строку и записываем в файл
    return write_everything

# Пример использования замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# После выполнения этого кода в файле example.txt будет:
# Это строчка
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']

# Часть 3: Класс MysticBall с методом __call__
class MysticBall:
    """
    Класс MysticBall для случайного выбора слов.
    """
    def __init__(self, *words):
        """
        Инициализация объекта с коллекцией слов.
        :param words: Коллекция строк для случайного выбора.
        """
        self.words = words

    def __call__(self):
        """
        Метод __call__, который позволяет использовать объект как функцию.
        :return: Случайно выбранное слово из коллекции.
        """
        return choice(self.words)

# Пример использования класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Случайный выбор слова из коллекции
print(first_ball())
print(first_ball())

# Ожидаемый результат (может отличаться из-за случайности):
# Да
# Нет
# Наверное

""" Пояснения:
Lambda-функция:
Используем map для применения функции ко всем парам символов из строк.
Функция lambda x, y: x == y возвращает True, если символы x и y совпадают.

Замыкание:
Внешняя функция get_advanced_writer принимает имя файла и возвращает вложенную функцию write_everything.
write_everything записывает все переданные данные в файл. Для преобразования данных в строку используется str().

Класс MysticBall:
Метод __call__ позволяет вызывать объект класса как функцию.
choice(self.words) возвращает случайное слово из списка words."""