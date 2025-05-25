from tkinter import ttk, simpledialog, messagebox
from EntryEx import EntryEx


class AskNameDialog(simpledialog.Dialog):
    """ Расширенный диалог ввода string """
    result: str
    
    def body(self, master):
        ttk.Label(master, text="Введите название эксперимента:").pack()
        self.e1 = EntryEx(master)
        self.e1.pack(expand=True, fill="both")
        return self.e1

    def apply(self):
        self.result = self.e1.get()
        if len(self.result) > 100:
            messagebox.showwarning("Ошибка", "Слишком длинный ввод!")
        if self.result.replace(' ', '') == '':
            messagebox.showwarning("Ошибка", "Пустой ввод!")