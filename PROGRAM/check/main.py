from tkinter import *
from tkinter import ttk, messagebox

from copypaste import *
from ListNotebook import *
from MeasForm import *
from ExpressionForm import *

from Models import *
from meas import *


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.current_exp = None
        self.title("Выберите эксперимент...")
        self.minsize(600, 300)
        self.create_menu()
        self.create_widgets()
        
        self.load_experiments()
    
    def create_widgets(self):
        # Панель действий
        self.bottom_frame = Frame(self, height=50)
        self.bottom_frame.pack_propagate(False)
        self.bottom_frame.pack(side="bottom", fill="x", expand=False)
        
        # ListNotebook
        self.note = ListNotebook()
        
        # Пустая форма
        self.empty_frame = ttk.Frame(self)
        ttk.Button(self.empty_frame, text="Новый эксперимент", command=self.new_experiment).pack(expand=True)
        self.note.basic_frame(self.empty_frame)
        
        # Форма добавления Measurement
        self.add_frame = MeasForm(self, self.create_measurement)
        c = lambda frame=self.add_frame: self.note.open_frame(frame)
        ttk.Button(self.bottom_frame, text="Добавить", command=c).grid(row=0, column=0)
        self.edit_menu.add_cascade(label="Добавить", command=c)
        self.note.basic_frame(self.add_frame)
        
        # Форма вычисления выражения
        self.expr_form = ExpressionForm(self, self.create_measurement, self.note.items)
        c = lambda frame=self.expr_form: self.note.open_frame(frame)
        ttk.Button(self.bottom_frame, text="Выражение", command=c).grid(row=0, column=1)
        self.edit_menu.add_cascade(label="Выражение", command=c)
        self.note.basic_frame(self.expr_form)
        
        # Кнопка удаления
        ttk.Button(self.bottom_frame, text="Удалить", command=self.delete_measurement).grid(row=0, column=2)
        self.edit_menu.add_cascade(label="Удалить", command=self.delete_measurement)

    def create_menu(self):
        self.option_add("*tearOff", FALSE)
        
        self.exp_menu = Menu()
        self.edit_menu = Menu()
        
        self.file_menu = Menu()
        self.file_menu.add_cascade(label="База данных...", command=self.choose_bd)
        self.file_menu.add_separator()
        self.file_menu.add_cascade(label="Новый эксперимент", command=self.new_experiment)
        self.file_menu.add_cascade(label="Удалить эксперимент", command=self.delete_experiment)      
        self.file_menu.add_cascade(label="Эксперимент", menu=self.exp_menu)

        menu = Menu()
        menu.add_cascade(label="Файл", menu=self.file_menu)
        menu.add_cascade(label="Правка", menu=self.edit_menu)
        menu.add_cascade(label="Справка", command=self.reference)
        self.config(menu=menu)
    
    """ Информационные сообщения """
    
    def choose_bd(self):
        messagebox.showinfo(title="База данных", message=f"Используемая база данных: {PATH}")
        
    def reference(self):
        messagebox.showinfo("Справка", "Разработчик: Сакулин Иван Михайлович (467335)")
    
    """ Управление экспериментами """
    
    def new_experiment(self):
        result = AskNameDialog(self, "Новый эксперимент").result
        if result is not None:
            exp = Experiment.create(name=result)
            self.load_experiments()
            self.open_experiment(exp)
            
    def delete_experiment(self):
        if self.current_exp is not None:
            result = messagebox.askokcancel("Удаление", "Удалить эксперимент?")
            if result:
                Experiment.delete_by_id(self.current_exp.exp_id)
                self.note.clear()
                self.title("Выберите эксперимент...")
                self.note.notebook.select(self.empty_frame)
                self.load_experiments()     
    
    def load_experiments(self):
        self.exp_menu.delete(0, END)
        for exp in Experiment.select():
            self.exp_menu.add_radiobutton(label=exp.name, command=lambda exp=exp: self.open_experiment(exp))
        if Experiment.select():
            self.file_menu.entryconfigure(3, state=NORMAL)
            self.file_menu.entryconfigure(4, state=NORMAL)
            self.open_experiment(exp)
        else:
            self.file_menu.entryconfigure(3, state=DISABLED)
            self.file_menu.entryconfigure(4, state=DISABLED)
        
    def open_experiment(self, exp):
        self.note.clear()
        self.current_exp = exp
        self.title(exp.name)
        for m in Meas.select().where((Meas.exp_id == exp.exp_id) & (Meas.name.is_null(False))):
            ms = Measurement(m.value, m.delta, m.epsilon, m.name, m.char, m.unit, direct=m.direct)
            ms.mid = m.meas_id
            self.load_measurement(ms)
        self.note.notebook.select(self.add_frame)
    
    """ Управление списком измерений """
    
    def create_measurement(self, _, m: Measurement):
        m.mid = Meas.create(exp_id=self.current_exp, name=m.name, char=m.char, unit=m.unit,
                    value=m.value_, delta=m.delta_, epsilon=m.epsilon_, direct=m.is_direct).meas_id
        self.load_measurement(m)
    
    def edit_measurement(self, old: Measurement, m: Measurement):
        meas = Meas.get(Meas.meas_id == old.mid)
        meas.name=m.name
        meas.char=m.char
        meas.unit=m.unit
        meas.value=m.value_
        meas.delta=m.delta_
        meas.epsilon=m.epsilon_
        meas.direct=m.is_direct
        meas.save()
        self.note.update_listbox(m)
    
    def delete_measurement(self):
        ret = self.note.pop()
        if ret is None:
            return
        if isinstance(ret, Measurement):
            Meas.delete_by_id(ret.mid)
    
    def load_measurement(self, m: Measurement):
        frame = MeasForm(self, self.edit_measurement, m)
        self.note.add(frame)
        
        
if __name__ == "__main__":
    PATH = "test.db"
    db.init(PATH)
    db.create_tables(tables)
    root = MainWindow()
    root.mainloop()
    