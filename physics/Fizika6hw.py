import matplotlib.pyplot as plt
import numpy as np

# Функция для вычисления спектральной светимости
def spectral_radiance(f, T):
    return f**3 / (np.exp(f/T) - 1)  # Формула Больцмана

# Диапазон частот
freq_range = np.arange(100, 20001, 100)

# Температуры
temperatures = [500, 1000, 1500, 2000, 2500]

# Построение графиков спектральной светимости
plt.figure(figsize=(10, 6))
for T in temperatures:
    radiance_values = [spectral_radiance(f, T) for f in freq_range]  # Расчет светимости
    plt.plot(freq_range, radiance_values, label=f'T={T}K')  # График

plt.title('Зависимость спектральной светимости от частот и температур')
plt.xlabel('Частот, f')
plt.ylabel('Спектральная светимость, r')
plt.legend()
plt.grid(True)
plt.show()

# Поиск частоты fmax при максимальной светимости
fmax_values = []
for T in temperatures:
    radiance_values = [spectral_radiance(f, T) for f in freq_range]  # Расчет светимости
    fmax = freq_range[np.argmax(radiance_values)]  # Частота с максимальной светимостью
    fmax_values.append(fmax)

# График зависимости T / fmax от температуры
plt.figure(figsize=(6, 6))
plt.plot(temperatures, np.divide(temperatures, fmax_values), marker='o')  # Нормализованные значения
plt.title('Проверка закона Вина: T / fmax = const')
plt.xlabel('Температура, T')
plt.ylabel('T / fmax')
plt.grid(True)
plt.show()

# Проверка закона Стефана–Больцмана
total_energy = [np.sum([spectral_radiance(f, T) for f in freq_range]) for T in temperatures]  # Сумма светимостей

# График зависимости суммарной светимости от T^4
plt.figure(figsize=(6, 6))
plt.plot(np.power(temperatures, 4), total_energy, marker='o')  # Зависимость
plt.title('Проверка зак. Стефана–Больцмана')
plt.xlabel('T^4')
plt.ylabel('Суммарная светимост')
plt.grid(True)
plt.show()
