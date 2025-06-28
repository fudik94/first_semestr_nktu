def rectangle_integration(func, lower_bound, upper_bound, num_segments):
    """
    Вычисление определенного интеграла методом центральных прямоугольников.

    :param func: Интегрируемая функция
    :param lower_bound: Нижняя граница отрезка интегрирования
    :param upper_bound: Верхняя граница отрезка интегрирования
    :param num_segments: Количество кусочков, на которые разбивается отрезок интегрирования
    :return: Приближенное значение определенного интеграла
    """
    segment_width = (upper_bound - lower_bound) / num_segments  # Ширина сегмента
    integral_sum = 0  # Сумма интеграла

    for i in range(num_segments):  # Проходим по всем сегментам
        x = lower_bound + i * segment_width + segment_width / 2  # Центральная точка сегмента
        integral_sum += func(x)  # Добавляем значение функции

    result = integral_sum * segment_width  # Приближенное значение интеграла
    return result  # Возвращаем результат

# Пример использования:
import math  # Импортируем библиотеку math

# Задаем функцию для тестирования (например, квадратичная функция)
def sample_function(x):
    return x**2  # Возвращаем квадрат x

# Задаем границы отрезка интегрирования и количество кусочков
a = 0  # Нижняя граница
b = 1  # Верхняя граница
n = 100  # Количество сегментов

# Вычисляем значение определенного интеграла
result = rectangle_integration(sample_function, a, b, n)  # Вызываем функцию интегрирования

# Выводим результат
print(f"Приближенное значение интеграла: {result}")  # Печатаем результат
