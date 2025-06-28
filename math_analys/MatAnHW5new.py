import random
import math

def monte_carlo_integration(func, lower, upper, num_samples):
    count_inside = 0

    # Максимальное значение функции на интервале [lower, upper] для синуса равно 1
    max_func_value = 1  # Для sin(x) на интервале [0, pi] максимум = 1

    for _ in range(num_samples):
        x = random.uniform(lower, upper)  # Случайное значение x
        y = random.uniform(0, max_func_value)  # Случайное значение y

        if 0 <= y <= func(x):  # Проверка, находится ли точка под графиком функции
            count_inside += 1

    area_rectangle = (upper - lower) * max_func_value  # Площадь прямоугольника
    ratio_inside = count_inside / num_samples  # Соотношение точек внутри

    return area_rectangle * ratio_inside  # Приближенное значение интеграла

# Функция для тестирования
def sine_function(x):
    return math.sin(x)

# Устанавливаем границы и количество точек
a = 0
b = math.pi
n = 10000  # Увеличьте количество точек для улучшения точности

# Вычисление интеграла
result = monte_carlo_integration(sine_function, a, b, n)
print("Приближенное значение определенного интеграла:", result)
