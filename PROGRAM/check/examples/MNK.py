import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import asyncio
import meas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор МНК")
        self.geometry("800x600")
        self.create_widgets()
        self.update_info()

    def create_widgets(self):
        # Левая панель
        left_frame = ttk.Frame(self, padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Текстовое поле с прокруткой
        self.text = tk.Text(left_frame, wrap=tk.NONE, width=20)
        scroll = ttk.Scrollbar(left_frame, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)
        
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Привязка валидации
        self.text.bind("<<Modified>>", self.validate_input)

        # Правая панель
        right_frame = ttk.Frame(self, padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Информационная панель
        info_frame = ttk.Frame(right_frame)
        info_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.count_label = ttk.Label(info_frame, text="Количество значений: 0")
        self.a_label = ttk.Label(info_frame, text=f"A")
        self.b_label = ttk.Label(info_frame, text=f"B")
        self.eq_label = ttk.Label(info_frame, text="Уравнение: y = Ax + B")
        
        self.count_label.pack(anchor=tk.W)
        self.a_label.pack(anchor=tk.W)
        self.b_label.pack(anchor=tk.W)
        self.eq_label.pack(anchor=tk.W)

        # График
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, right_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Меню
        main_menu = tk.Menu()
        main_menu.add_cascade(label="Сохранить график", command=self.save_plot)
        main_menu.add_cascade(label="Справка", command=self.help)

        self.config(menu=main_menu)

    def help(self):
        tk.messagebox.showinfo("Справка", 'Создатель этого "шедевра" Сакулин Иван Михайлович. Вводите в новой строке значения через пробел: X Y.')


    def validate_input(self, event):
        if not self.text.edit_modified():
            return
        
        text = self.text.get("1.0", tk.END)
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
        
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", "\n".join(valid_lines))
        self.text.edit_modified(False)
        
        self.update_info()

    def update_info(self):
        text = self.text.get("1.0", tk.END)
        values = [line.strip().split() for line in text.splitlines() if len(line.split()) == 2 and line.split()[1] != '-']
        
        try:
            # Рассчёт
            dmm = meas.LinearMultipleMeasurement(
                [float(v[0]) for v in values],
                [float(v[1]) for v in values]
            )
            
            # Обновление информации
            self.count_label.config(text=f"Количество значений: {dmm._N}")
            self.a_label.config(text=f"Угловой коэффициент: {dmm._b.rounded}")
            self.b_label.config(text=f"Свободный член: {dmm._a.rounded}")
            self.eq_label.config(text=f"Уравнение: y = {dmm._b.value}x + {dmm._a.value}")
            
            meas.Drawer().plot_MKN(fig=self.figure, ax=self.ax, data=dmm)
            self.canvas.draw()
            
        except meas.MeasException as e:
            self.count_label.config(text=e)
            self.a_label.config(text=f"Угловой коэффициент K")
            self.b_label.config(text=f"Свободный член A")
            self.eq_label.config(text=f"Уравнение: y = Kx + A")
            self.ax.clear()

    def save_plot(self):
        path = tk.filedialog.asksaveasfilename(
            initialdir = "/",title = "Сохранение",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
            )
        self.figure.savefig(path)


if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    