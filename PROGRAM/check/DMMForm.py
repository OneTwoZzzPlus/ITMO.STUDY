from tkinter import *
from tkinter import ttk
from EntryEx import EntryEx
from SaveMeasFrame import SaveMeasFrame
from meas import DirectMultipleMeasurement, MeasException, StudentException
from typing import Callable
import re

float_re = re.compile(r'^[+-]?(\d+([.]\d*)?([eE][+-]?\d+)?|\.\d+([eE][+-]?\d+)?)$')

            
class DMMForm(ttk.Frame):
    dmm: DirectMultipleMeasurement|None
    
    def __init__(self, master: Misc|None, apply_command: Callable, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_measurement = apply_command
        self.dmm = None
        self._create_widgets()
        self.update_info()

    def _create_widgets(self):
        # Левая панель
        self.left_frame = ttk.Frame(self, padding=10)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Текстовое поле с прокруткой
        self.text = Text(self.left_frame, wrap=NONE, width=20)
        scroll = ttk.Scrollbar(self.left_frame, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        scroll.pack(side=RIGHT, fill=Y)

        # Правая панель
        self.right_frame = ttk.Frame(self, padding=10)
        self.right_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Инструментальная погрешность
        self.delta_form = ttk.LabelFrame(self.right_frame, 
                                         text="Инструментальная погрешность")
        self.delta_var = StringVar(self.delta_form, value="")
        self.delta_entry = EntryEx(self.delta_form, textvariable=self.delta_var)
        self.delta_entry.configure(
            validate="key",
            validatecommand=(self.register(self._validate_float), '%P')
        )
        self.delta_entry.pack(fill=X, expand=True, padx=5, pady=5)
        self.delta_form.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        # Вывод результата
        self.result_form = ttk.LabelFrame(self.right_frame, text="Результат")
        self.result_var = StringVar(self.result_form, value="Введите значения!")
        self.result_label = ttk.Label(self.result_form, textvariable=self.result_var)
        self.result_label.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.result_form.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        # Сохранение
        self.meas_form = SaveMeasFrame(self.right_frame, self._create_meas, 
                                       text="Сохранение результата")
        self.meas_form.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        # Привязка валидации
        self.text.bind("<<Modified>>", self._validate_input)
        
    def _validate_input(self, event):
        """ Валидация списка значений """
        if not self.text.edit_modified():
            return
        
        position = self.text.index(INSERT)
        text = self.text.get("1.0", END)
        lines = text.splitlines()
        valid_lines = []
        
        for line in lines:
            if line in ["-", ""]:
                valid_lines.append(line.strip())
                continue
            try:
                float(line)
                valid_lines.append(line)
            except ValueError:
                continue
        
        self.text.delete("1.0", END)
        self.text.insert("1.0", "\n".join(valid_lines))
        self.text.edit_modified(False)
        self.text.mark_set("insert", position)
        
        self.update_info()

    def update_info(self):
        """ Перерасчёт результата измерения """
        text = self.text.get("1.0", END)
        values = [
            float(line) for line in text.splitlines() if line not in ["-", ""]
        ]
        try:
            try:
                delta_ins = float(self.delta_var.get())
            except ValueError:
                delta_ins = 0
            self.dmm = DirectMultipleMeasurement(values, delta_ins)
            self.result_var.set(self.dmm.rounded)
        except StudentException as e:
            self.result_var.set(e)
            self.dmm = None
        except MeasException as e:
            self.dmm = None
            self.result_var.set("Введите значения!")
        
    def _validate_float(self, value: str):
        """ Валидация ввода для float значений """
        return float_re.match(value) is not None or value in ["", "-"] 
    
    def _create_meas(self, name: str, char: str, unit: str):
        """ Привязка имени, символа и единицы измерения к результату """
        if self.dmm is None:
            return
        self.dmm.name = name
        self.dmm.char = char
        self.dmm.unit = unit
        self.create_measurement(None, self.dmm.asMeasurment)
