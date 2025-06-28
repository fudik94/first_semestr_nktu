def simpsons_integration(func, lower, upper, segments):
    """
    Вычисляет определенный интеграл функции методом Симпсона.

    :param func: Интегрируемая функция
    :param lower: Нижняя граница отрезка интегрирования
    :param upper: Верхняя граница отрезка интегрирования
    :param segments: Количество кусочков (разбиений), должно быть четным
    :return: Приближенное значение определенного интеграла
    """
    if segments % 2 != 0:  # Проверка на четность количества сегментов
        raise ValueError("Количество кусочков (segments) должно быть четным для метода Симпсона")

    step_size = (upper - lower) / segments  # Ширина сегмента
    integral_total = func(lower) + func(upper)  # Начальная сумма с краев

    for i in range(1, segments, 2):  # Нечетные индексы
        integral_total += 4 * func(lower + i * step_size)  # Добавляем значения для нечетных индексов

    for i in range(2, segments-1, 2):  # Четные индексы
        integral_total += 2 * func(lower + i * step_size)  # Добавляем значения для четных индексов

    return integral_total * step_size / 3  # Возвращаем результат интегрирования

# Пример использования:
def quadratic_function(x):
    return x**2  # Возвращаем квадрат x

# Устанавливаем границы интегрирования и количество сегментов
a = 0  # Нижняя граница
b = 1  # Верхняя граница
n = 1000  # Количество сегментов (четное)

# Вычисляем значение определенного интеграла
result = simpsons_integration(quadratic_function, a, b, n)  # Вызываем функцию интегрирования
print("Приближенное значение определенного интеграла:", result)  # Печатаем результат
