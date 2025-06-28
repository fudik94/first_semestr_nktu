import numpy as np
import matplotlib.pyplot as plt

# Функция для построения фигуры Лиссажу
def plot_lissajous(A1, A2, n, t_max=2 * np.pi, points=1000):
    # Временной диапазон
    t = np.linspace(0, t_max, points)
    
    # Вычисление координат x и y
    x = A1 * np.cos(t)
    y = A2 * np.sin(n * t)
    
    # Построение графика
    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.title(f"Фигура Лиссажу (n = {n})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis('equal')  # Сохранение пропорций осей
    plt.show()

# Пример использования функции
A1 = 1   # Амплитуда по оси x
A2 = 1   # Амплитуда по оси y
n = 3/2  # Отношение частот

plot_lissajous(A1, A2, n)
