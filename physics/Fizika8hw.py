import numpy as np
import matplotlib.pyplot as plt

def random_walk(N, num_trials):
    mean_square_displacement = np.zeros(N + 1)

    for _ in range(num_trials):
        positions = np.zeros(N + 1)

        for step in range(1, N + 1):
            # Случайное блуждание по оси Ox
            positions[step] = positions[step - 1] + np.random.normal()

        mean_square_displacement += positions**2

    mean_square_displacement /= num_trials

    return mean_square_displacement

def plot_random_walk():
    np.random.seed(42)  # Для воспроизводимости результатов

    max_N = 50
    num_trials = 500

    N = 10
    mean_square_displacement = random_walk(N, num_trials)

    # Построение графика
    steps = [step for step in range(N + 1)]
    plt.plot(steps, mean_square_displacement, label=f'N={N}')

    plt.xlabel('Число шагов (N)')
    plt.ylabel('Средний квадрат смещения (S^2)')
    plt.legend()
    plt.show()

# Вызываем функцию без явного условия if __name__ == "__main__":
plot_random_walk()