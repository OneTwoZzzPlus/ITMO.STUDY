from tkinter import *
from tkinter import ttk
from copypaste import *
from Models import *
from meas import *
from MeasForm import *


class ListNotebook(Frame): 
    """ Отображает коллекцию и формы взаимодействия с ними """
    def __init__(self):
        super().__init__()
        self.frames = []
        self.items = []
        self.shift = 0
        
        # NOTEBOOK
        self.notebook = ttk.Notebook(self)
        ttk.Style(self).layout("TNotebook.Tab", [])            
        self.notebook.pack(expand=True, side="right", fill="both")
        
        # LISTBOX
        self.left_frame = Frame(self, width=180)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side="left", fill="y", expand=False)
        self.listbox = Listbox(self.left_frame)
        
        # scroll для listbox
        scrollbar = ttk.Scrollbar(self.listbox, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox["yscrollcommand"]=scrollbar.set
        
        def selected(event):
            """ Переключение вкладок """
            if len(self.listbox.curselection()) != 0:
                tab = self.listbox.curselection()[0]
                self.current_tab = tab
                self.notebook.select(self.shift + tab)
        
        self.listbox.bind("<<ListboxSelect>>", selected)    
        self.listbox.pack(expand=True, fill="both")
        
        self.pack(expand=True, side="top", fill="both")

    def basic_frame(self, frame: ttk.Frame):
        """ Добавляет основные формы, не привязанные к измерениям """
        self.shift += 1
        self.notebook.add(frame)
        
    def open_frame(self, frame):
        """ Открывает форму программно """
        self.notebook.select(frame)

    def add(self, frame: ttk.Frame):
        """ Добавляет измерения и их формы """
        element = frame.old_meas
        self.frames.append(frame)
        self.items.append(element)
        self.listbox.insert(END, element.name)
        self.notebook.add(frame)
        
    def update_listbox(self, element):
        """ Обновляет пункты меню listbox """
        index = self.current_tab
        self.items[index] = element
        self.listbox.delete(index)
        self.listbox.insert(index, self.items[index].name)
        
    def delete(self, index: int):
        """ Удаляет пункт списка измерений по индексу """
        self.listbox.delete(index)
        self.notebook.forget(self.frames[index])
        self.frames.pop(index)
        self.items.pop(index)
        
    def pop(self):
        """ Удаляет текущий выбранный пункт списка измерений """
        if self.listbox.curselection():
            tab = self.listbox.curselection()[0]
            ret = self.items[tab]
            self.delete(tab)
            return ret
        return None
            
    def clear(self):
        """ Очистка списка измерений """
        for i in range(len(self.items) - 1, -1, -1):
            self.delete(i)