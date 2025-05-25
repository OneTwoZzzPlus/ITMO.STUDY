from tkinter import *
from tkinter import ttk
from EntryEx import EntryEx
from typing import Callable


class GraphicSettingsFrame(ttk.LabelFrame):
    def __init__(self, master: Misc|None, apply_command: Callable, 
                 save_command: Callable, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.apply_command = apply_command
        self.save_command = save_command
        self._create_widgets()

    def _create_widgets(self):
        # Инициализация переменных
        self.x_name_var = StringVar(value="X")
        self.y_name_var = StringVar(value="Y")
        self.x_unit_var = StringVar(value="")
        self.y_unit_var = StringVar(value="")
        self.pad_x_var = DoubleVar(value=1.35)
        self.pad_y_var = DoubleVar(value=1.65)
        self.error_x_var = BooleanVar(value=False)
        self.error_y_var = BooleanVar(value=False)

        # Строка 0: Названия осей
        self.x_name_label = ttk.Label(self, text="Название X:")
        self.x_name_label.grid(row=0, column=0, padx=2, pady=2, sticky=W)
        
        self.x_name_entry = EntryEx(self, textvariable=self.x_name_var, width=15)
        self.x_name_entry.grid(row=0, column=1, padx=2, pady=2)
        
        self.y_name_label = ttk.Label(self, text="Название Y:")
        self.y_name_label.grid(row=0, column=2, padx=2, pady=2, sticky=W)
        
        self.y_name_entry = EntryEx(self, textvariable=self.y_name_var, width=15)
        self.y_name_entry.grid(row=0, column=3, padx=2, pady=2)

        # Строка 1: Единицы измерения
        self.x_unit_label = ttk.Label(self, text="Единицы X:")
        self.x_unit_label.grid(row=1, column=0, padx=2, pady=2, sticky=W)
        
        self.x_unit_entry = EntryEx(self, textvariable=self.x_unit_var, width=15)
        self.x_unit_entry.grid(row=1, column=1, padx=2, pady=2)
        
        self.y_unit_label = ttk.Label(self, text="Единицы Y:")
        self.y_unit_label.grid(row=1, column=2, padx=2, pady=2, sticky=W)
        
        self.y_unit_entry = EntryEx(self, textvariable=self.y_unit_var, width=15)
        self.y_unit_entry.grid(row=1, column=3, padx=2, pady=2)

        # Строка 2: Отступы
        self.pad_x_label = ttk.Label(self, text="Отступ X:")
        self.pad_x_label.grid(row=2, column=0, padx=2, pady=2, sticky=W)
        
        self.pad_x_slider = ttk.Scale(
            self, from_=0.9, to=2.0, variable=self.pad_x_var,
            orient=HORIZONTAL, length=120
        )
        self.pad_x_slider.grid(row=2, column=1, padx=2, pady=2)
        
        self.pad_y_label = ttk.Label(self, text="Отступ Y:")
        self.pad_y_label.grid(row=2, column=2, padx=2, pady=2, sticky=W)
        
        self.pad_y_slider = ttk.Scale(
            self, from_=0.9, to=2.0, variable=self.pad_y_var,
            orient=HORIZONTAL, length=120
        )
        self.pad_y_slider.grid(row=2, column=3, padx=2, pady=2)

        # Строка 3: Чекбоксы
        self.error_x_check = ttk.Checkbutton(
            self,
            text="Ошибки X",
            variable=self.error_x_var
        )
        self.error_x_check.grid(row=3, column=0, columnspan=2, 
                                padx=2, pady=2, sticky=W)
        
        self.error_y_check = ttk.Checkbutton(
            self,
            text="Ошибки Y",
            variable=self.error_y_var
        )
        self.error_y_check.grid(row=3, column=2, columnspan=2, 
                                padx=2, pady=2, sticky=W)

        # Строка 4: Кнопки
        self.apply_button = ttk.Button(self, text="Применить", 
                                       command=self.apply_command)
        self.apply_button.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        
        self.clear_button = ttk.Button(self, text="Сбросить", 
                                       command=self.clear_form)
        self.clear_button.grid(row=4, column=2, padx=5, pady=5, sticky="ew")
        
        self.save_button = ttk.Button(self, text="Сохранить график", 
                                      command=self.save_command)
        self.save_button.grid(row=4, column=3, padx=5, pady=5, sticky="ew")
        
        # Настройка веса колонок для растяжения
        for i in range(4):
            self.columnconfigure(i, weight=1)
            
    def clear_form(self):
        """ Очистка/сброс всех полей ввода """
        self.x_name_var.set("X")
        self.y_name_var.set("Y")
        self.x_unit_var.set("")
        self.y_unit_var.set("")
        self.pad_x_var.set(1.35)
        self.pad_y_var.set(1.65)
        self.error_x_var.set(False)
        self.error_y_var.set(False)