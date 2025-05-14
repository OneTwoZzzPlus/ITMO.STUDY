from tkinter import *
from tkinter import ttk


class ListNotebook(Frame): 
    def __init__(self):
        super().__init__()
        self.frames = []
        
        # NOTEBOOK
        self.notebook = ttk.Notebook(self)
        ttk.Style(self).layout("TNotebook.Tab", [])            
        self.notebook.pack(expand=True, side="right", fill="both")
        
        # LISTBOX
        self.left_frame = Frame(self, width=180)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side="left", fill="y", expand=False)

        self.listbox = Listbox(self.left_frame)
        
        # прокрутка
        scrollbar = ttk.Scrollbar(self.listbox, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox["yscrollcommand"]=scrollbar.set
        
        def selected(event):
            if self.listbox.size() != 0:
                tab = self.listbox.curselection()[0]
                self.notebook.select(tab)
        
        self.listbox.bind("<<ListboxSelect>>", selected)    
        self.listbox.pack(expand=True, fill="both")
        
        self.pack(expand=True, side="top", fill="both")

    def add(self, element: str|list[str]):
        if isinstance(element, list):
            for x in element:
                self.add(x)
            return # для добавления списка
        
        frame = ttk.Frame(self)
        ttk.Button(frame, text=element).pack(expand=True, fill="both")
        self.frames.append(frame)
        
        self.listbox.insert(END, element)
        self.notebook.add(frame)
        
    def delete(self, index: int):
        self.listbox.delete(index)
        self.notebook.forget(self.frames[index])


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("MainWindow")
        self.minsize(600, 300)
        self.option_add("*tearOff", FALSE)
        
        # MENU
        file_menu = Menu()
        file_menu.add_cascade(label="Новый", command=self.new_file)
        file_menu.add_cascade(label="Открыть", command=self.open_file)
        file_menu.add_cascade(label="Сохранить", command=self.save_file)
        
        edit_menu = Menu()
        edit_menu.add_cascade(label="Добавить", command=self.add_meas)
        edit_menu.add_cascade(label="DMM", command=self.add_DMM)
        edit_menu.add_cascade(label="LMM", command=self.add_LMM)
        edit_menu.add_cascade(label="Удалить", command=self.del_meas)
        
        menu = Menu()
        menu.add_cascade(label="Файл", menu=file_menu)
        menu.add_cascade(label="Правка", menu=edit_menu)
        menu.add_cascade(label="Справка", command=self.reference)
        self.config(menu=menu)
        
        # HOTKEYS
        self.bind('<Control-n>', lambda x: self.new_file())
        self.bind('<Control-o>', lambda x: self.open_file())
        self.bind('<Control-s>', lambda x: self.save_file())
        
        # BOTTOM FRAME
        self.bottom_frame = Frame(self, height=50)
        self.bottom_frame.pack_propagate(False)
        ttk.Button(self.bottom_frame, text="Добавить", command=self.add_meas).grid(row=1, column=1)
        ttk.Button(self.bottom_frame, text="DMM", command=self.add_DMM).grid(row=1, column=2)
        ttk.Button(self.bottom_frame, text="LMM", command=self.add_LMM).grid(row=1, column=3)
        ttk.Button(self.bottom_frame, text="Удалить", command=self.del_meas).grid(row=1, column=4)
        self.bottom_frame.pack(side="bottom", fill="x", expand=False)
        
        # TOP FRAME
        self.top_frame = ListNotebook()
        self.top_frame.add(list(map(str, range(10)))) 
        
    def new_file(self):
        print('new_file')
        
    def open_file(self):
        print('open_file')
        
    def save_file(self):
        print('save_file')
    
    def add_meas(self):
        print('add_meas')
        
    def add_DMM(self):
        print('add_DMM')
        
    def add_LMM(self):
        print('add_LMM')
        
    def del_meas(self):
        print('del_meas')
        
    def reference(self):
        print('Справка')
        
        
if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
    