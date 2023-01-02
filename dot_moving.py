import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.animation import FuncAnimation as Fnc

t, T = sp.Symbol('t'), np.linspace(1, 15, 1000)

r, phi = 2 + sp.sin(6 * t), 6.5 * t + 1.2 * sp.cos(6 * t)   # 15 variant
x, y = r * sp.cos(phi), r * sp.sin(phi)

Vx, Vy = sp.diff(x, t), sp.diff(y, t)
Wx, Wy = sp.diff(Vx, t), sp.diff(Vy, t)
V, W = sp.sqrt(Vx ** 2 + Vy ** 2), sp.sqrt(Wx ** 2 + Wy ** 2)

F_func = [sp.lambdify(t, i) for i in [x, y, Vx, Vy, Wx, Wy]]
[X, Y, Vx, Vy, Wx, Wy] = [func(T) for func in F_func]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal'), ax.set_title("Модель движения точки"), ax.set_xlabel('x'), ax.set_ylabel('y'), ax.plot(X, Y), ax.set(
    xlim=[-5, 5], ylim=[-5, 5])

P = ax.plot(X[0], Y[0], marker='*')[0]
kf, flag = 0.1, 1


def moving(i):
    P.set_data(X[i], Y[i])
    vline = ax.arrow(X[i], Y[i], kf * Vx[i], kf * Vy[i], width=0.02, color=(1, 0, 0.7),
                     label='- скорость')
    wline = ax.arrow(X[i], Y[i], kf * Wx[i], kf * Vy[i], width=0.02, color=(0, 0.5, 1),
                     label='- ускорение')
    cvector = ax.arrow(X[i], Y[i], - kf * ((Vy[i] * (Vx[i] ** 2 + Vy[i] ** 2)) / (Vx[i] * Wy[i] - Wx[i] * Vy[i])),
                       kf * ((Vx[i] * (Vx[i] ** 2 + Vy[i] ** 2)) / (Vx[i] * Wy[i] - Wx[i] * Vy[i])),
                       width=0.03, color=(0.5, 0.5, 0.5), label='- кривизна')
    global flag
    if flag:
        ax.legend(ncol=2,
                  facecolor=(0.3, 1, 0.4),
                  edgecolor=(0, 0, 1),
                  title='обозначение векторов',
                  title_fontsize='10')
        flag = False

    return P, vline, wline, cvector


move = Fnc(fig=fig, func=moving, frames=len(T), interval=10, blit=True)

plt.show()
