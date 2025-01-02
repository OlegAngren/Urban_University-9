# Пользовательский класс исключения StepValueError
# Наследуемся от стандартного класса ValueError и используем pass, чтобы оставить класс пустым
class StepValueError(ValueError):
    pass

# Класс Iterator реализует пользовательский итератор
class Iterator:
    def __init__(self, start, stop, step=1):
        """
        Конструктор класса.

        :param start: Начало итерации (целое число).
        :param stop: Конец итерации (целое число).
        :param step: Шаг итерации (целое число, по умолчанию 1).
        """
        if step == 0:
            # Если шаг равен 0, выбрасываем исключение StepValueError
            raise StepValueError('шаг не может быть равен 0')

        # Инициализация атрибутов объекта
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Текущая позиция итератора

    def __iter__(self):
        """
        Метод для сброса pointer и возврата самого объекта итератора.
        """
        self.pointer = self.start  # Сбрасываем pointer на начальное значение
        return self

    def __next__(self):
        """
        Метод для перехода к следующему элементу итерации.

        :return: Текущее значение pointer перед увеличением.
        :raises StopIteration: Если pointer выходит за пределы итерации.
        """
        # Проверяем, завершена ли итерация в зависимости от знака шага
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        # Сохраняем текущее значение pointer для возврата
        current = self.pointer
        # Увеличиваем pointer на шаг step
        self.pointer += self.step
        return current

# Пример использования
try:
    iter1 = Iterator(100, 200, 0)  # Шаг равен 0, должно быть выброшено исключение
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

# Создаем несколько объектов класса Iterator с разными параметрами
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Итерация через объекты с использованием цикла for
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
