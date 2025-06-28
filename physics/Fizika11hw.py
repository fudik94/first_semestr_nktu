import numpy as np
import matplotlib.pyplot as plt

m = 1.0
k = 10.0
gamma = 0.5
F0 = 1.0
omega = 2.0

x0 = 1.0
v0 = 0.0

dt = 0.01
num_steps = 1000

x = np.zeros(num_steps)
v = np.zeros(num_steps)
t = np.linspace(0, num_steps * dt, num_steps)

x[0] = x0
v[0] = v0

for i in range(1, num_steps):
    a = -(k / m) * x[i - 1] - (gamma / m) * \
        v[i - 1] + (F0 / m) * np.cos(omega * t[i - 1])
    v[i] = v[i - 1] + a * dt
    x[i] = x[i - 1] + v[i - 1] * dt

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, x, label='Position x(t)', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Position x')
plt.title('Forced Oscillations: Position vs Time')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, v, label='Phase trajectory', color='orange')
plt.xlabel('Position x')
plt.ylabel('Velocity v')
plt.title('Phase Trajectory of Forced Oscillations')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
