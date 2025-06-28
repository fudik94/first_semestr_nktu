import math

# Функция для расчета времени
def calculate_time(x, a, b, v1, v2):
    time_to_C = math.sqrt(a**2 + x**2) / v1  # Время от A до C
    time_to_B = math.sqrt(b**2 + (a - x)**2) / v2  # Время от C до B
    return time_to_C + time_to_B  # Общее время

# Функция для проверки закона преломления
def law_of_refraction(x, a, b, n1, n2):
    alpha = math.atan(x / a)  # Угол входа
    beta = math.atan((b - x) / math.sqrt(b**2 + (a - x)**2))  # Угол выхода
    
    # Проверка закона Ферма
    if math.isclose(math.sin(alpha) / math.sin(beta), n2 / n1):
        return n1 * math.sin(alpha), n2 * math.sin(beta)  # Вернуть значения
    else:
        raise ValueError("Закон преломления не выполнен")  # Ошибка, если закон не соблюдается

# Исходные данные
a = 3  # Расстояние от A до границы
b = 4  # Расстояние от B до границы
v1 = 1  # Скорость света в первой среде
v2 = 1.5  # Скорость света во второй среде
n1 = 1.5  # Показатель преломления первой среды
n2 = 2.0  # Показатель преломления второй среды

# Генерация значений x для расчета времени
x_values = [i / 10 for i in range(int((a + b) * 10) + 1)]

# Расчет времени и функций для каждого x
time_values = [calculate_time(x, a, b, v1, v2) for x in x_values]
f1_values, f2_values = zip(*[law_of_refraction(x, a, b, n1, n2) for x in x_values])

# Нахождение кратчайшего пути
optimal_x = x_values[time_values.index(min(time_values))]
min_time = min(time_values)

# Вывод результатов
print(f"Кратчайший путь (по времени) находится при x = {optimal_x}")
print(f"Минимум время прохождения света: {min_time} секунд")
