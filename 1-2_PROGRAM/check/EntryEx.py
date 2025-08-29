from tkinter import ttk, Menu


class EntryEx(ttk.Entry):
    """ Расширенный entry с функциями cut/copy/paste """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = Menu(self, tearoff=False)
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