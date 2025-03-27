from math import *

import matplotlib.pyplot

from .tools import *
from .LinearMultipleMeasurement import *
import matplotlib
from matplotlib.ticker import AutoLocator
import numpy as np


def plot_controller(method_to_decorate):
    plt = matplotlib.pyplot
    
    def wrapper(self, *args):
        return method_to_decorate(self, plt, *args)

    plt.tight_layout()
    plt.show()
    
    return wrapper


class Drawer():
    
    @plot_controller
    def plot_dependency(self, plt, nA, nB, X, Y):
        # Создаем фигуру и оси
        (fig, ax) = plt.subplots(figsize=(8, 8))
        
        # Считаем границы
        X_min, X_max = min(X), max(X)
        Y_min, Y_max = min(Y), max(Y)
        
        # Экспериментальные точки с погрешностями
        ax.errorbar(x=[point.value for point in X], 
                    y=[point.value for point in Y], 
                    xerr=[point.delta for point in X], 
                    yerr=[point.delta for point in Y],
                    fmt='o', color='blue', markersize=6,
                    label='Экспериментальные точки', capsize=3)
        
        # Теоретическая зависимость
        Z_range = np.linspace(X_min.value - X_min.delta, X_max.value + X_max.delta)
        Y_theor = nA * Z_range + nB
        ax.plot(Z_range, Y_theor, 'r-', label=f'Теория: Y = {nA:.2f}X + {nB:.2f}')
        
        # Устанавливаем пределы осей
        w_x, w_y = 0, 0
        ax.set_xlim(X_min.value - X_min.delta - 0.05*(X_max.value - X_min.value) - w_x, X_max.value + X_max.delta + 0.05*(X_max.value - X_min.value) + w_x)
        ax.set_ylim(Y_min.value - Y_min.delta - 0.05*(Y_max.value - Y_min.value) - w_y, Y_max.value + Y_max.delta + 0.05*(Y_max.value - Y_min.value) + w_y)
        # Подписи осей
        plt.xlabel("Z", x=1.01, ha='right', va='bottom', 
                bbox={
                    'boxstyle': 'square',  # стиль рамки (круглая/прямоугольная)
                    'facecolor': 'white', # цвет фона
                    'edgecolor': 'white', # цвет рамки
                    'pad': 1.15            # отступ текста от рамки
                })
        plt.ylabel("X", y=1.01, ha='left', va='top', rotation=0, 
                bbox={
                    'boxstyle': 'square',  # стиль рамки (круглая/прямоугольная)
                    'facecolor': 'white', # цвет фона
                    'edgecolor': 'white', # цвет рамки
                    'pad': 1.65            # отступ текста от рамки
                })
        # Настройка делений сетки
        ax.xaxis.set_major_locator(AutoLocator())
        ax.yaxis.set_major_locator(AutoLocator())
        # Включаем сетку
        plt.grid(True, which='both', linestyle='--', alpha=0.7)
        # Добавляем заголовок
        plt.title('График зависимости Y(X)')
        