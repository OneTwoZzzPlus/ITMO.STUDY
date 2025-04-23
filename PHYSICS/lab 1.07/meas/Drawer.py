from math import *
from .tools import *
from .LinearMultipleMeasurement import *

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np
import asyncio


def plot_controller(method_to_decorate):
    
    async def wrapper(self, *args, **kwargs):
        await method_to_decorate(self, *args, **kwargs)
    
    plt.show()
    
    return wrapper


class Drawer():
    
    @plot_controller
    async def plot_dependency(self, 
            nA:Measurement, nB:Measurement, X:list[Measurement], Y:list[Measurement],
            x_name='X', x_unit='', y_name='Y', y_unit='',
            label: str=None, pad_x=1.35, pad_y=1.65,
            error_X=False, error_Y=False, 
        ):
        if label is None:
            label = f'График зависимости: {y_name}({x_name})'
            
        print(f'График зависимости: {y_name} = {nA.value}{'+' if nB.value >= 0 else ''}{nB.value}{x_name}')
        
        # Создаем фигуру и оси
        (fig, ax) = plt.subplots(figsize=(8, 8))
        
        # Считаем границы
        X_min, X_max = min(X), max(X)
        Y_min, Y_max = min(Y), max(Y)
        
        # Экспериментальные точки с 
        xerr = [point.delta for point in X] if error_X else None
        yerr = [point.delta for point in Y] if error_Y else None
        ax.errorbar(x=[point.value for point in X], 
                    y=[point.value for point in Y], 
                    xerr=xerr, 
                    yerr=yerr,
                    fmt='o', color='blue', markersize=6,
                    label='Экспериментальные точки', capsize=3)
        
        # Теоретическая зависимость
        X_range = np.linspace(X_min.value - X_min.delta, X_max.value + X_max.delta)
        Y_theor = nA.value_ + X_range * nB.value_
        ax.plot(X_range, Y_theor, 'r-', label=label)
        
        # Устанавливаем пределы осей
        w_x, w_y = 0, 0
        m_x, m_y = 0.05*(X_max.value - X_min.value), 0.05*(Y_max.value - Y_min.value)
        ax.set_xlim(
            float(min(X_min.value - X_min.delta - m_x - w_x, min(X_range)-m_x)), 
            float(max(X_max.value + X_max.delta + m_x + w_x, max(X_range)+m_x))
            )
        # print(Y_min.value - Y_min.delta - 0.05*(Y_max.value - Y_min.value) - w_y, Y_max.value + Y_max.delta + 0.05*(Y_max.value - Y_min.value) + w_y)
        ax.set_ylim(
            float(min(Y_min.value - Y_min.delta - m_y - w_y, min(Y_theor)-m_y)), 
            float(max(Y_max.value + Y_max.delta + m_y + w_y, max(Y_theor)+m_y))
            )
        # Подписи осей
        plt.xlabel(f'{x_name}{'' if x_unit == '' else f', {x_unit}'}', x=1.01, ha='right', va='bottom', 
                bbox={
                    'boxstyle': 'square',  # стиль рамки (круглая/прямоугольная)
                    'facecolor': 'white', # цвет фона
                    'edgecolor': 'white', # цвет рамки
                    'pad': pad_x           # отступ текста от рамки
                })
        plt.ylabel(f'{y_name}{'' if y_unit == '' else f', {y_unit}'}', y=1.01, ha='left', va='top', rotation=0, 
                bbox={
                    'boxstyle': 'square',  # стиль рамки (круглая/прямоугольная)
                    'facecolor': 'white', # цвет фона
                    'edgecolor': 'white', # цвет рамки
                    'pad': pad_y            # отступ текста от рамки
                })
        # Настройка делений сетки
        ax.xaxis.set_major_locator(AutoLocator())
        ax.yaxis.set_major_locator(AutoLocator())
        # Включаем сетку
        plt.grid(True, which='both', linestyle='--', alpha=0.7)
        # Добавляем заголовок
        plt.title(label)
        plt.tight_layout()