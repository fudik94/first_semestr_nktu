def trapezoidal_integration(func, lower, upper, segments):
    """
    Вычисляет определенный интеграл функции методом трапеций.

    :param func: Интегрируемая функция
    :param lower: Нижняя граница отрезка интегрирования
    :param upper: Верхняя граница отрезка интегрирования
    :param segments: Количество кусочков (разбиений)
    :return: Приближенное значение определенного интеграла
    """
    step_size = (upper - lower) / segments  # Ширина каждого сегмента
    integral_total = 0.5 * (func(lower) + func(upper))  # Начальная сумма с краев

    for i in range(1, segments):  # Цикл по сегментам
        integral_total += func(lower + i * step_size)  # Добавляем значение функции

    return integral_total * step_size  # Возвращаем результат интегрирования

# Пример использования:
def quadratic_function(x):
    return x**2  # Возвращаем квадрат x

# Устанавливаем границы интегрирования и количество сегментов
a = 0  # Нижняя граница
b = 1  # Верхняя граница
n = 1000  # Количество сегментов

# Вычисляем значение определенного интеграла
result = trapezoidal_integration(quadratic_function, a, b, n)  # Вызываем функцию интегрирования
print("Приближенное значение определенного интеграла:", result)  # Печатаем результат
