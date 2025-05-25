from tkinter import *
from tkinter import ttk, messagebox
from EntryEx import *
from meas import Measurement, expression, ExpressionError
from typing import Callable

            
class ExpressionForm(ttk.Frame):
    measurments_list: list[Measurement]
    
    def __init__(self, master: Misc | None, apply_command: Callable, 
                 measurments_list: list[Measurement], *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._create_widgets()
        self.measurments_list = measurments_list
        self.apply_command = apply_command

    def _create_widgets(self):
        # Подпись
        self.name_label = ttk.Label(self, text="Ввод выражения")
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="")
        
        # Name (обязательное, до 80 символов)
        self.name_label = ttk.Label(self, text="Название*")
        self.name_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = EntryEx(self)
        self.name_entry.grid(row=2, column=1, columnspan=3, 
                             padx=5, pady=5, sticky="ew")
        self.name_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 80), '%P')
        )

        # Char (до 40 символов)
        self.char_label = ttk.Label(self, text="Символ")
        self.char_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.char_entry = EntryEx(self)
        self.char_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.char_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 40), '%P')
        )

        # Unit (до 40 символов)
        self.unit_label = ttk.Label(self, text="Ед. изм.")
        self.unit_label.grid(row=3, column=2, padx=5, pady=5, sticky="e")
        self.unit_entry = EntryEx(self)
        self.unit_entry.grid(row=3, column=3, padx=5, pady=5, sticky="ew")
        self.unit_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 40), '%P')
        )

        # Expression (обязательное)
        self.expression_label = ttk.Label(self, text="Выражение")
        self.expression_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.expression_entry = EntryEx(self)
        self.expression_entry.grid(row=4, column=1, columnspan=3, 
                                   padx=5, pady=5, sticky="ew")

        # Кнопки
        self.apply_button = ttk.Button(self, text="Рассчитать", 
                                       command=self.apply)
        self.apply_button.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
        
        self.clear_button = ttk.Button(self, text="Отмена", 
                                       command=self.clear_form)
        self.clear_button.grid(row=5, column=2, padx=5, pady=5, sticky="ew")
        
        # Расширение кнопок
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def clear_form(self):
        """ Очистка всех полей ввода """
        self.name_entry.delete(0, END)
        self.unit_entry.delete(0, END)
        self.char_entry.delete(0, END)
        self.expression_entry.delete(0, END)
    
    def apply(self):
        """ Обработка нажатия кнопки сохранения """
        try:
            name = self.name_entry.get()
            if name.replace(' ', '') == '':
                raise ExpressionError("Имя обязательно!")
            
            char = self.char_entry.get()
            unit = self.unit_entry.get()
            
            expr = self.expression_entry.get()
            if expr.replace(' ', '') == '':
                raise ExpressionError("Выражение обязательно!")
            
            ret = expression(self.measurments_list, expr, name, char, unit)
            
            self.apply_command(None, ret)
            
        except ExpressionError as e:
            messagebox.showwarning("Некорректное выражение", str(e))
        except Exception as e:
            messagebox.showerror("Неожиданная ошибка!", str(e))
            print(e)