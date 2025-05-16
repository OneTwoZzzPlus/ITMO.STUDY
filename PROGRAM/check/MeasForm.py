from tkinter import *
from tkinter import ttk, messagebox
from Models import *
from meas import *
from copypaste import *
import re
            
            
class MeasForm(ttk.Frame):
    def __init__(self, master=None, apply_command=None, meas: Measurement|None=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.float_re = re.compile(r'^[+-]?(\d+([.]\d*)?([eE][+-]?\d+)?|\.\d+([eE][+-]?\d+)?)$')
        self.create_widgets()
        self.apply_command = apply_command
        self.add_button.config(command=self.apply)
        self.old_meas = meas
        if meas is not None:
            self.fill(meas)
        if meas is None:
            self.clear_button.config(text="Очистить")

    def create_widgets(self):
        self.name_label = ttk.Label(self, text="Простое измерение")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="")
        
        shift_row = 1
        # Name (обязательное, до 80 символов)
        self.name_label = ttk.Label(self, text="Название*")
        self.name_label.grid(row=shift_row+1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = EntryEx(self)
        self.name_entry.grid(row=shift_row+1, column=1, columnspan=3, padx=5, pady=5, sticky="ew")
        self.name_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 80), '%P')
        )

        # Char (до 40 символов)
        self.char_label = ttk.Label(self, text="Символ")
        self.char_label.grid(row=shift_row+2, column=0, padx=5, pady=5, sticky="e")
        self.char_entry = EntryEx(self)
        self.char_entry.grid(row=shift_row+2, column=1, padx=5, pady=5, sticky="ew")
        self.char_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 40), '%P')
        )

        # Unit (до 40 символов)
        self.unit_label = ttk.Label(self, text="Ед. изм.")
        self.unit_label.grid(row=shift_row+2, column=2, padx=5, pady=5, sticky="e")
        self.unit_entry = EntryEx(self)
        self.unit_entry.grid(row=shift_row+2, column=3, padx=5, pady=5, sticky="ew")
        self.unit_entry.configure(
            validate="key",
            validatecommand=(self.register(lambda text: len(text) <= 40), '%P')
        )

        # Value (обязательное float)
        self.value_label = ttk.Label(self, text="Значение*")
        self.value_label.grid(row=shift_row+3, column=0, padx=5, pady=5, sticky="e")
        self.value_entry = EntryEx(self)
        self.value_entry.grid(row=shift_row+3, column=1, columnspan=3, padx=5, pady=5, sticky="ew")
        self.value_entry.configure(
            validate="key",
            validatecommand=(self.register(self.validate_float), '%P')
        )

        # Delta (float)
        self.delta_label = ttk.Label(self, text="Абс. погрешность")
        self.delta_label.grid(row=shift_row+4, column=0, padx=5, pady=5, sticky="e")
        self.delta_entry = EntryEx(self)
        self.delta_entry.grid(row=shift_row+4, column=1, padx=5, pady=5, sticky="ew")
        self.delta_entry.configure(
            validate="key",
            validatecommand=(self.register(self.validate_float), '%P')
        )

        # Epsilon (float)
        self.epsilon_label = ttk.Label(self, text="Отн. погрешность")
        self.epsilon_label.grid(row=shift_row+4, column=2, padx=5, pady=5, sticky="e")
        self.epsilon_entry = EntryEx(self)
        self.epsilon_entry.grid(row=shift_row+4, column=3, padx=5, pady=5, sticky="ew")
        self.epsilon_entry.configure(
            validate="key",
            validatecommand=(self.register(self.validate_float), '%P')
        )

        # Dim (float)
        self.dim_label = ttk.Label(self, text="Множитель")
        self.dim_label.grid(row=shift_row+5, column=0, padx=5, pady=5, sticky="e")
        self.dim_entry = EntryEx(self)
        self.dim_entry.grid(row=shift_row+5, column=1, padx=5, pady=5, sticky="ew")
        self.dim_entry.configure(
            validate="key",
            validatecommand=(self.register(self.validate_float), '%P')
        )

        # Checkbox is_direct (по умолчанию True)
        self.is_direct_var = BooleanVar(value=True)
        self.is_direct_check = ttk.Checkbutton(
            self, 
            text="Прямое измерение", 
            variable=self.is_direct_var, 
            onvalue=True, 
            offvalue=False
        )
        self.is_direct_check.grid(row=shift_row+5, column=3, padx=5, pady=5, sticky="w")

        # Кнопки
        self.add_button = ttk.Button(self, text="Сохранить")
        self.add_button.grid(row=shift_row+6, column=1, padx=5, pady=5, sticky="ew")
        
        self.clear_button = ttk.Button(self, text="Отмена", command=self.clear_form)
        self.clear_button.grid(row=shift_row+6, column=2, padx=5, pady=5, sticky="ew")
        
        # Расширение кнопок
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def validate_float(self, value):
        """ Валидация ввода для float значений """
        return self.float_re.match(value) is not None or value in ["", "-"] 

    def clear_form(self):
        """ Очистка/сброс всех полей ввода """
        self.name_entry.delete(0, END)
        self.unit_entry.delete(0, END)
        self.char_entry.delete(0, END)
        self.value_entry.delete(0, END)
        self.delta_entry.delete(0, END)
        self.epsilon_entry.delete(0, END)
        self.dim_entry.delete(0, END)
        self.is_direct_var.set(True)
        
        # Заполнение полей в случае редактирования
        if self.old_meas is not None:
            self.fill(self.old_meas)
    
    def apply(self):
        """ Обработка нажатия кнопки сохранения """
        try:
            name = self.name_entry.get()
            if name.replace(' ', '') == '':
                raise Exception("Имя обязательно!")
            
            value = self.value_entry.get()
            if value in ['', '-']:
                raise Exception("Значение обязательно!")
            
            delta, epsilon, dim = self.delta_entry.get(), self.epsilon_entry.get(), self.dim_entry.get()
            delta = None if delta in ["", "-"] else float(delta)
            epsilon = None if epsilon in ["", "-"] else float(epsilon)
            dim = None if dim in ["", "-"] else float(dim)
            
            m = Measurement(
                float(value),
                delta,
                epsilon,
                name,
                self.char_entry.get(),
                self.unit_entry.get(),
                dim,
                self.is_direct_var.get()
            )
            self.apply_command(self.old_meas, m)
            if self.old_meas is not None:
                m.mid = self.old_meas.mid
                self.old_meas = m
        except ValueError as e:
            messagebox.showwarning("Ошибка", "Некорректный ввод")
            print(e)
        except Exception as e:
            messagebox.showwarning("Ошибка", str(e))
            print(e)

    def fill(self, meas: Measurement):
        """ Заполнение форм """
        self.name_entry.insert(0, meas.name)
        self.unit_entry.insert(0, "" if meas.unit is None else meas.unit)
        self.char_entry.insert(0, "" if meas.char is None else meas.char)
        self.value_entry.insert(0, meas.value)
        self.delta_entry.insert(0, meas.delta)
        self.epsilon_entry.insert(0, meas.epsilon)
        self.dim_entry.configure(state=DISABLED)
        self.is_direct_var.set(meas.is_direct)