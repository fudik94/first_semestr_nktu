def compute_derivative(x_vals, delta_x, func_vals):
    # Инициализация массива для значений производной
    derivative_vals = []

    for i in range(len(x_vals)):
        x_current = x_vals[i]  # Текущая точка
        h = delta_x  # Шаг

        if i == 0:  # Начальная точка
            derivative = (-func_vals[i + 2] + 4 * func_vals[i + 1] - 3 * func_vals[i]) / (2 * h)
        elif i == len(x_vals) - 1:  # Конечная точка
            derivative = (func_vals[i - 2] - 4 * func_vals[i - 1] + 3 * func_vals[i]) / (2 * h)
        else:  # Внутренняя точка
            derivative = (func_vals[i + 1] - func_vals[i - 1]) / (2 * h)

        derivative_vals.append(derivative)  # Добавляем значение производной

    return derivative_vals  # Возвращаем массив значений производной

# Пример использования:
import matplotlib.pyplot as plt  # Импортируем библиотеку для построения графиков

# Задаем функцию для тестирования (например, квадратичная функция)
def sample_function(x):
    return x**2  # Возвращаем квадрат x

# Задаем диапазон и шаг
x_vals = [i for i in range(-10, 11)]  # Генерируем список значений x
step_size = 1  # Устанавливаем шаг

# Вычисляем значения функции для каждой точки x
func_vals = [sample_function(x) for x in x_vals]  # Вычисляем значения функции

# Вычисляем значения производной
derivative_vals = compute_derivative(x_vals, step_size, func_vals)  # Вычисляем производные

# Выводим результаты
print("Значения функции:", func_vals)  # Печатаем значения функции
print("Значения производной:", derivative_vals)  # Печатаем значения производной

# Рисуем графики
plt.plot(x_vals, func_vals, label='Функция')  # График функции
plt.plot(x_vals, derivative_vals, label='Производная')  # График производной
plt.legend()  # Добавляем легенду
plt.show()  # Показываем график


#func_vals = [100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#x_vals = [i for i in range(-10, 11)]  # Список от -10 до 10
