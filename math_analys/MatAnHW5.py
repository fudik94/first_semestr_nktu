import random  # Импортируем библиотеку random для генерации случайных чисел

def monte_carlo_integration(func, lower, upper, num_samples):
    """
    Вычисляет определенный интеграл функции методом Монте-Карло.

    :param func: Интегрируемая функция
    :param lower: Нижняя граница отрезка интегрирования
    :param upper: Верхняя граница отрезка интегрирования
    :param num_samples: Количество случайных точек для метода Монте-Карло
    :return: Приближенное значение определенного интеграла
    """
    count_inside = 0  # Счетчик точек внутри функции

    for _ in range(num_samples):  # Генерация случайных точек
        x = random.uniform(lower, upper)  # Случайное значение x
        y = random.uniform(0, max(func(lower), func(upper)))  # Случайное значение y

        if 0 <= y <= func(x):  # Проверка, находится ли точка под графиком функции
            count_inside += 1  # Увеличиваем счетчик, если точка внутри

    area_rectangle = (upper - lower) * max(func(lower), func(upper))  # Площадь прямоугольника
    ratio_inside = count_inside / num_samples  # Соотношение точек внутри

    return area_rectangle * ratio_inside  # Возвращаем результат

# Пример использования:
import math  # Импортируем библиотеку math для математических функций

def sine_function(x):
    return math.sin(x)  # Возвращаем значение синуса

# Устанавливаем границы интегрирования и количество случайных точек
a = 0  # Нижняя граница
b = math.pi  # Верхняя граница
n = 10000  # Количество случайных точек

# Вычисляем значение определенного интеграла
result = monte_carlo_integration(sine_function, a, b, n)  # Вызываем функцию интегрирования
print("Приближенное значение определенного интеграла:", result)  # Печатаем результат
