import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Определение дифференциального уравнения
def oscillator(y, t, gamma, omega0):
    theta, omega = y
    dydt = [omega, -2 * gamma * omega - omega0 ** 2 * np.sin(theta)]
    return dydt

# Параметры
gamma = 0.3  # Коэффициент сухого трения
omega0 = 2.0  # Угловая частота без трения
y0 = [0.5, 0.0]  # Начальные условия: начальный угол и начальная угловая скорость
t = np.linspace(0, 20, 1000)  # Временной интервал

# Решение дифференциального уравнения
sol = odeint(oscillator, y0, t, args=(gamma, omega0))

# Извлечение угла и угловой скорости из решения
theta = sol[:, 0]
omega = sol[:, 1]

# Новые начальные условия
y0_new = [-0.5, 0.0]

# Решение дифференциального уравнения с новыми начальными условиями
sol_new = odeint(oscillator, y0_new, t, args=(gamma, omega0))

# Извлечение угла и угловой скорости из решения с новыми начальными условиями
theta_new = sol_new[:, 0]
omega_new = sol_new[:, 1]

# Построение графика угловой скорости от угла отклонения
plt.figure()
plt.plot(theta, omega, 'b', label='Угловая скорость')
plt.plot(theta_new, omega_new, 'r', label='Угловая скорость')
plt.xlabel('Угол отклонения')
plt.ylabel('Угловая скорость')
# plt.legend(loc='best')
plt.grid()
plt.title('Фазовый портрет системы с сухим трением')
# Добавление осей координат
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('auto')
plt.show()
