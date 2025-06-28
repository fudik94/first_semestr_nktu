import numpy as np  
import matplotlib.pyplot as plt  

def spring_pendulum_damped(mass, spring_constant, damping_coefficient, initial_displacement, initial_velocity, time_step, num_steps):
    # Инициализация массивов для хранения данных
    displacement = np.zeros(num_steps)  # Массив смещений
    velocity = np.zeros(num_steps)  # Массив скоростей
    time = np.zeros(num_steps)  # Массив времени

    # Установка начальных условий
    displacement[0] = initial_displacement  # Начальное смещение
    velocity[0] = initial_velocity  # Начальная скорость

    # Итерационное моделирование движения пружинного маятника
    for i in range(1, num_steps):  # Цикл по шагам времени
        time[i] = time[i-1] + time_step  # Обновляем время
        # Вычисляем ускорение
        acceleration = (-spring_constant * displacement[i-1] - damping_coefficient * velocity[i-1]) / mass
        velocity[i] = velocity[i-1] + acceleration * time_step  # Обновляем скорость
        displacement[i] = displacement[i-1] + velocity[i] * time_step  # Обновляем смещение

    return time, displacement, velocity  # Возвращаем время, смещение и скорость

# Параметры пружинного маятника
mass = 0.4  # Масса маятника
spring_constant = 100.0  # Жесткость пружины
damping_coefficient = 2  # Коэффициент затухания

# Начальные условия
initial_displacement = 0.3  # Начальное смещение
initial_velocity = 1  # Начальная скорость

# Параметры моделирования
time_step = 0.01  # Шаг времени
num_steps = 1000  # Количество шагов

# Моделирование
time, displacement, velocity = spring_pendulum_damped(mass, spring_constant, damping_coefficient, initial_displacement, initial_velocity, time_step, num_steps)

# Построение фазовой кривой
plt.plot(displacement, velocity)  # Рисуем фазовую кривую
plt.title('Фазовая кривая пружинного маятника с затуханием')  # Заголовок графика
plt.xlabel('x')  # Подпись оси X
plt.ylabel('v(x)')  # Подпись оси Y
plt.grid()  # Включаем сетку
plt.show()  # Показываем график
