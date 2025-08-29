from tkinter import *
from tkinter import ttk, messagebox
from EntryEx import EntryEx
from typing import Callable


class SaveMeasFrame(ttk.LabelFrame):
    def __init__(self, master: Misc|None, 
                 apply_command: Callable, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.apply_command = apply_command
        self._create_widgets()

    def _create_widgets(self):
        # Name (обязательное, до 80 символов)
        self.name_label = ttk.Label(self, text="Название*")
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = EntryEx(self)
        self.name_entry.grid(row=1, column=1, columnspan=3, 
                             padx=5, pady=5, sticky="ew")
        self.name_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 80), '%P')
        )

        # Char (до 40 символов)
        self.char_label = ttk.Label(self, text="Символ")
        self.char_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.char_entry = EntryEx(self)
        self.char_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.char_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 40), '%P')
        )
        
        # Unit (до 40 символов)
        self.unit_label = ttk.Label(self, text="Ед. изм.")
        self.unit_label.grid(row=2, column=2, padx=5, pady=5, sticky="e")
        self.unit_entry = EntryEx(self)
        self.unit_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
        self.unit_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 40), '%P')
        )

        # Кнопки
        self.add_button = ttk.Button(self, text="Создать", 
                                     command=self.apply)
        self.add_button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        self.clear_button = ttk.Button(self, text="Очистить", 
                                       command=self.clear_form)
        self.clear_button.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
        
        # Расширение кнопок
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def clear_form(self):
        """ Очистка/сброс всех полей ввода """
        self.name_entry.delete(0, END)
        self.unit_entry.delete(0, END)
        self.char_entry.delete(0, END)
    
    def apply(self):
        """ Обработка нажатия кнопки сохранения """
        try:
            name = self.name_entry.get()
            if name.replace(' ', '') == '':
                raise ValueError("Имя обязательно!")
            
            self.apply_command(name, 
                               self.char_entry.get(), 
                               self.unit_entry.get()
                               )
        
        except ValueError as e:
            messagebox.showwarning("Ошибка ввода", str(e))
            print(e)