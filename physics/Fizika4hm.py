import math

# Метод золотого сечения для поиска минимума функции
def golden_section_search(func, a, b, tol=1e-5):
    phi = (1 + math.sqrt(5)) / 2  # Золотое сечение
    resphi = 2 - phi

    # Начальные точки для поиска
    x1 = b - resphi * (b - a)
    x2 = a + resphi * (b - a)

    f1 = func(x1)  # Значение функции в x1
    f2 = func(x2)  # Значение функции в x2

    # Цикл для сужения интервала
    while math.fabs(b - a) > tol:
        if f1 < f2:
            b = x2  # Сужаем правую границу
            x2 = x1
            f2 = f1
            x1 = b - resphi * (b - a)  # Новая x1
            f1 = func(x1)
        else:
            a = x1  # Сужаем левую границу
            x1 = x2
            f1 = f2
            x2 = a + resphi * (b - a)  # Новая x2
            f2 = func(x2)

    return (a + b) / 2  # Возвращаем среднюю точку

# Функция для расчета времени
def calculate_time(x, a, b, v1, v2):
    time_to_C = math.sqrt(a**2 + x**2) / v1  # Время от A до C
    time_to_B = math.sqrt(b**2 + (a - x)**2) / v2  # Время от C до B
    return time_to_C + time_to_B  # Общее время

# Исходные данные
a = 3  # Расстояние от A до границы
b = 4  # Расстояние от B до границы
v1 = 1  # Скорость света в первой среде
v2 = 1.5  # Скорость света во второй среде

# Поиск оптимального x для минимизации времени
x_optimal = golden_section_search(lambda x: calculate_time(x, a, b, v1, v2), 0, a + b)

min_time = calculate_time(x_optimal, a, b, v1, v2)  # Минимальное время

# Вывод результатов
print(f"Оптимальное положение точки C (x): {x_optimal}")
print(f"Минимум время прохождения света: {min_time} секунд")
