def apply_all_func(int_list, *functions):
    """
    Применяет все переданные функции к списку чисел и возвращает словарь результатов.

    :param int_list: список из чисел (int, float).
    :param functions: функции для применения к списку.
    :return: словарь с результатами, где ключи - имена функций, значения - результаты выполнения.
    """
    results = {}
    for func in functions:
        try:
            results[func.__name__] = func(int_list)
        except Exception as e:
            results[func.__name__] = f"Ошибка: {e}"
    return results

# Пример использования
if __name__ == "__main__":
    numbers = [6, 20, 15, 9]
    print(apply_all_func(numbers, max, min))  # Пример с max и min
    print(apply_all_func(numbers, len, sum, sorted))  # Пример с len, sum и sorted
