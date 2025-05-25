from tkinter import *
from tkinter import ttk

from EntryEx import *
from MeasForm import *


class ListNotebook(Frame):
    """ Отображает коллекцию и формы взаимодействия с ними """
    _frames: list[ttk.Frame]
    _items: list[Measurement]
    _shift: int
    _current_tab: int|None
    
    @property
    def items(self):
        return self._items
    
    def __init__(self):
        super().__init__()
        self._frames = []
        self._items = []
        self._shift = 0
        
        # NOTEBOOK
        self.notebook = ttk.Notebook(self)
        ttk.Style(self).layout("TNotebook.Tab", [])            
        self.notebook.pack(expand=True, side="right", fill="both")
        
        # LISTBOX
        self.left_frame = ttk.Frame(self, width=180)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side="left", fill="y", expand=False)
        self.listbox = Listbox(self.left_frame)
        
        # Scrollbar для Listbox
        scrollbar = ttk.Scrollbar(self.listbox, orient="vertical", 
                                  command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox["yscrollcommand"]=scrollbar.set
        
        def selected(event):
            """ Переключение вкладок """
            if len(self.listbox.curselection()) != 0:
                tab = self.listbox.curselection()[0]
                self._current_tab = tab
                self.notebook.select(self._shift + tab)
        
        self.listbox.bind("<<ListboxSelect>>", selected)    
        self.listbox.pack(expand=True, fill="both")

    def basic_frame(self, frame: ttk.Frame):
        """ Добавляет основные формы, не привязанные к измерениям """
        self._shift += 1
        self.notebook.add(frame)
        
    def open_frame(self, frame: ttk.Frame):
        """ Открывает форму программно """
        self.notebook.select(frame)

    def add(self, frame: MeasForm):
        """ Добавляет измерения и их формы """
        element = frame.current_meas
        self._frames.append(frame)
        self._items.append(element)
        self.listbox.insert(END, element.name)
        self.notebook.add(frame)
        
    def update_listbox(self, element: Measurement):
        """ Обновляет пункты меню listbox """
        index = self._current_tab
        self._items[index] = element
        self.listbox.delete(index)
        self.listbox.insert(index, self._items[index].name)
        
    def delete(self, index: int):
        """ Удаляет пункт списка измерений по индексу """
        self.listbox.delete(index)
        self.notebook.forget(self._frames[index])
        self._frames.pop(index)
        self._items.pop(index)
        
    def pop(self):
        """ Удаляет текущий выбранный пункт списка измерений """
        if self.listbox.curselection():
            tab = self.listbox.curselection()[0]
            ret = self._items[tab]
            self.delete(tab)
            return ret
        return None
            
    def clear(self):
        """ Очистка списка измерений """
        for i in range(len(self._items) - 1, -1, -1):
            self.delete(i)