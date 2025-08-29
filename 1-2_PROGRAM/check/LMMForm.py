from tkinter import *
from tkinter import ttk, filedialog, messagebox
from GraphicSettingsFrame import GraphicSettingsFrame
from SaveMeasFrame import SaveMeasFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from meas import LinearMultipleMeasurement, MeasException, Drawer
from typing import Callable
            
            
class LMMForm(ttk.Frame):
    lmm: LinearMultipleMeasurement|None
    
    def __init__(self, master: Misc|None, 
                 apply_command: Callable, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_measurement = apply_command
        self.lmm = None
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
        
        # Привязка валидации
        self.text.bind("<<Modified>>", self._validate_input)

        # Правая панель
        self.right_frame = ttk.Frame(self, padding=10)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Информационная панель
        info_frame = ttk.Frame(self.right_frame)
        info_frame.pack(side=TOP, fill=X)
        
        self.count_label = ttk.Label(info_frame, 
                                     text="Количество значений: 0")
        self.a_label = ttk.Label(info_frame, text=f"A")
        self.b_label = ttk.Label(info_frame, text=f"B")
        self.eq_label = ttk.Label(info_frame, 
                                  text="Уравнение: y = Ax + B")
        
        self.count_label.pack(anchor=W)
        self.a_label.pack(anchor=W)
        self.b_label.pack(anchor=W)
        self.eq_label.pack(anchor=W)

        # График
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, self.right_frame)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        # Центральная панель
        self.center_frame = ttk.Frame(self)
        self.center_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        # Фрейм конфигурации
        self.config_frame = GraphicSettingsFrame(
            self.center_frame, self._update_graphic, 
            self.save_plot, text="Настройка графика"
            )
        self.config_frame.pack(fill=BOTH, expand=True, pady=5)
        
        # Формы вывода коэффициентов
        self.a_frame = SaveMeasFrame(self.center_frame, 
                                     self._create_meas_a, 
                                     text="Свободный член")
        self.a_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.b_frame = SaveMeasFrame(self.center_frame, 
                                     self._create_meas_b, 
                                     text="Угловой коэффициент")
        self.b_frame.pack(fill=BOTH, expand=True, pady=5)
        
    def _validate_input(self, event):
        """ Валидация списка значений """
        if not self.text.edit_modified():
            return
        
        position = self.text.index(INSERT)
        text = self.text.get("1.0", END)
        lines = text.splitlines()
        valid_lines = []
        
        for line in lines:
            lsp = line.split()
            if len(lsp) < 2:
                valid_lines.append(line)
                continue
            if len(lsp) > 2:
                lsp = lsp[0:2]
            if lsp[1].strip() == "-":
                valid_lines.append(f'{lsp[0]} {lsp[1]}')
                continue
            try:
                float(lsp[0].strip())
                float(lsp[1].strip())
                valid_lines.append(line)
            except ValueError:
                continue
        
        self.text.delete("1.0", END)
        self.text.insert("1.0", "\n".join(valid_lines))
        self.text.edit_modified(False)
        self.text.mark_set("insert", position)
        
        self.update_info()

    def update_info(self):
        """ Перерасчёт результата """
        text = self.text.get("1.0", END)
        values = []
        for line in text.splitlines():
            if len(line.split()) == 2 and line.split()[1] != '-':
                values.append(line.strip().split())
        
        try:
            # Рассчёт
            x = [float(v[0]) for v in values]
            y = [float(v[1]) for v in values]
            self.lmm = LinearMultipleMeasurement(x, y)
            
            # Обновление информации
            self.count_label.config(
                text=f"Количество значений: {self.lmm._N}")
            self.a_label.config(
                text=f"Угловой коэффициент: {self.lmm.b.rounded}")
            self.b_label.config(
                text=f"Свободный член: {self.lmm.a.rounded}")
            self.eq_label.config(
                text=f"Уравнение: y = {self.lmm.b.value}x + {self.lmm.a.value}")
            
            self._update_graphic()
            
        except MeasException as e:
            self.count_label.config(text=e)
            self.a_label.config(text=f"Угловой коэффициент K")
            self.b_label.config(text=f"Свободный член A")
            self.eq_label.config(text=f"Уравнение: y = Kx + A")
            self.lmm = None
            self.ax.clear()

    def _update_graphic(self):
        """ Обновление графика """
        if self.lmm is None:
            return
        
        Drawer().plot_MKN(
            fig=self.figure, 
            ax=self.ax, 
            data=self.lmm,
            x_name=self.config_frame.x_name_var.get(),
            x_unit=self.config_frame.x_unit_var.get(),
            y_name=self.config_frame.y_name_var.get(),
            y_unit=self.config_frame.y_unit_var.get(),
            pad_x=self.config_frame.pad_x_var.get(),
            pad_y=self.config_frame.pad_y_var.get(),
            error_X=self.config_frame.error_x_var.get(),
            error_Y=self.config_frame.error_y_var.get()
            )
        self.canvas.draw()

    def _create_meas_a(self, name: str, char: str, unit: str):
        """ Сохранение измерения A """
        if self.lmm is None:
            return
        self.lmm.a.name = name
        self.lmm.a.char = char
        self.lmm.a.unit = unit
        self.create_measurement(None, self.lmm.a)
        
    def _create_meas_b(self, name: str, char: str, unit: str):
        """ Сохранение измерения B """
        if self.lmm is None:
            return
        self.lmm.b.name = name
        self.lmm.b.char = char
        self.lmm.b.unit = unit
        self.create_measurement(None, self.lmm.b)

    def save_plot(self):
        """ Сохранение графика """
        try:
            path = filedialog.asksaveasfilename(
                initialdir = "/",
                title = "Сохранение", 
                filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
            )
            self.figure.savefig(path)
        except PermissionError as e:
            messagebox.showerror("Ошибка", 
                                 "Недостаточно прав для сохранения!")
            print(e)
        except Exception as e:
            messagebox.showerror("Неожиданная ошибка", str(e))
            print(e)



