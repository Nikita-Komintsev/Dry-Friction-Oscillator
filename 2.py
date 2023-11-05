import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Определение дифференциального уравнения для линейной системы с затуханием меньше критического
def linear_oscillator(y, t, gamma, omega0):
    theta, omega = y
    dydt = [omega, -2 * gamma * omega - omega0 ** 2 * theta]
    return dydt

# Параметры для линейной системы с затуханием меньше критического
gamma_linear = 1.0  # Затухание меньше чем 2 * omega0
omega0_linear = 10.0  # Угловая частота
y0_linear = [0.50, 0.50]  # Начальные условия: начальный угол и начальная угловая скорость
t = np.linspace(0, 40, 4000)  # Увеличенный временной интервал с большим количеством точек

# Решение дифференциального уравнения для линейной системы с затуханием меньше критического
sol_linear = odeint(linear_oscillator, y0_linear, t, args=(gamma_linear, omega0_linear))

# Извлечение угла и угловой скорости из решения линейной системы с затуханием меньше критического
theta_linear = sol_linear[:, 0]
omega_linear = sol_linear[:, 1]

# Построение графика угловой скорости от угла отклонения для линейной системы с затуханием меньше критического
plt.figure()
plt.plot(theta_linear, omega_linear, 'b', label='Линейная система (затухание < 2*omega0)')
plt.xlabel('Угол отклонения')
plt.ylabel('Угловая скорость')
# plt.legend(loc='best')
plt.grid()
plt.title('Фазовый портрет с затуханием меньше критического')

# Добавление осей координат
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('auto')
plt.show()
