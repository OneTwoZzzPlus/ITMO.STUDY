import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class EntryEx(ttk.Entry):
    """ Расширенный entry с функциями cut/copy/paste """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label="Copy", command=self.popup_copy)
        self.menu.add_command(label="Cut", command=self.popup_cut)
        self.menu.add_command(label="Paste", command=self.popup_paste)
        self.bind("<Button-3>", self.display_popup)

    def display_popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def popup_copy(self):
        self.event_generate("<<Copy>>")

    def popup_cut(self):
        self.event_generate("<<Cut>>")

    def popup_paste(self):
        self.event_generate("<<Paste>>")
        

class AskNameDialog(simpledialog.Dialog):
    """ Расширенный диалог ввода string """
    def body(self, master):
        ttk.Label(master, text="Введите название эксперимента:").pack()
        self.e1 = EntryEx(master)
        self.e1.pack(expand=True, fill=tk.BOTH)
        return self.e1

    def apply(self):
        self.result = self.e1.get()
        if len(self.result) > 100:
            messagebox.showwarning("Ошибка", "Слишком длинный ввод!")
        if self.result.replace(' ', '') == '':
            messagebox.showwarning("Ошибка", "Пустой ввод!")