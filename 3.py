import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Определение дифференциального уравнения для линейной системы с затуханием больше критического
def over_damped_linear_oscillator(y, t, gamma, omega0):
    theta, omega = y
    dydt = [omega, -2 * gamma * omega - omega0 ** 2 * theta]
    return dydt

# Параметры для линейной системы с затуханием больше критического
gamma_over_damped_linear = 5.0  # Затухание больше чем 2 * omega0
omega0_linear = 5.0  # Угловая частота
y0_over_damped_linear = [-0.2, 5.0]  # Начальные условия: начальный угол и начальная угловая скорость
y0_additional_1 = [0.4, 5.0]  # Дополнительные начальные условия
y0_additional_2 = [1.2, 5.0]  # Дополнительные начальные условия
y0_additional_3 = [-0.2, -5.0]
y0_additional_4 = [0.2, -5.0]
y0_additional_5 = [-0.5, -5.0]
y0_additional_6 = [-1.2, -5.0]
t = np.linspace(0, 20, 1000)  # Временной интервал

# Решение дифференциального уравнения для линейной системы с затуханием больше критического
sol_over_damped_linear = odeint(over_damped_linear_oscillator, y0_over_damped_linear, t, args=(gamma_over_damped_linear, omega0_linear))
sol_additional_1 = odeint(over_damped_linear_oscillator, y0_additional_1, t, args=(gamma_over_damped_linear, omega0_linear))
sol_additional_2 = odeint(over_damped_linear_oscillator, y0_additional_2, t, args=(gamma_over_damped_linear, omega0_linear))
sol_additional_3 = odeint(over_damped_linear_oscillator, y0_additional_3, t, args=(gamma_over_damped_linear, omega0_linear))
sol_additional_4 = odeint(over_damped_linear_oscillator, y0_additional_4, t, args=(gamma_over_damped_linear, omega0_linear))
sol_additional_5 = odeint(over_damped_linear_oscillator, y0_additional_5, t, args=(gamma_over_damped_linear, omega0_linear))
sol_additional_6 = odeint(over_damped_linear_oscillator, y0_additional_6, t, args=(gamma_over_damped_linear, omega0_linear))

# Извлечение угла и угловой скорости из решения линейной системы с затуханием больше критического
theta_over_damped_linear = sol_over_damped_linear[:, 0]
omega_over_damped_linear = sol_over_damped_linear[:, 1]

# Извлечение угла и угловой скорости из решения дополнительных систем
theta_additional_1 = sol_additional_1[:, 0]
omega_additional_1 = sol_additional_1[:, 1]
theta_additional_2 = sol_additional_2[:, 0]
omega_additional_2 = sol_additional_2[:, 1]
theta_additional_3 = sol_additional_3[:, 0]
omega_additional_3 = sol_additional_3[:, 1]
theta_additional_4 = sol_additional_4[:, 0]
omega_additional_4 = sol_additional_4[:, 1]
theta_additional_5 = sol_additional_5[:, 0]
omega_additional_5 = sol_additional_5[:, 1]
theta_additional_6 = sol_additional_6[:, 0]
omega_additional_6 = sol_additional_6[:, 1]

# Построение графика угловой скорости от угла отклонения для всех трех систем
plt.figure()
plt.plot(theta_over_damped_linear, omega_over_damped_linear, 'g', label='Линейная система (затухание > 2*omega0)')
plt.plot(theta_additional_1, omega_additional_1, 'g', label='Дополнительная система 1')
plt.plot(theta_additional_2, omega_additional_2, 'g', label='Дополнительная система 2')
plt.plot(theta_additional_3, omega_additional_3, 'b', label='Дополнительная система 2')
plt.plot(theta_additional_4, omega_additional_4, 'b', label='Дополнительная система 2')
plt.plot(theta_additional_5, omega_additional_5, 'b', label='Дополнительная система 2')
plt.plot(theta_additional_6, omega_additional_6, 'b', label='Дополнительная система 2')
plt.xlabel('Угол отклонения')
plt.ylabel('Угловая скорость')

# Выделение осей
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Настройка масштаба и меток
plt.xlim(-2, 2)
plt.ylim(-10, 10)
plt.xticks(np.arange(-2, 2.1, 0.5))
plt.yticks(np.arange(-10, 11, 2))
plt.axis('auto')

plt.grid()
plt.title('Фазовый портрет с затуханием больше критического')
plt.show()
