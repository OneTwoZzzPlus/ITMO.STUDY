from tkinter import *
from tkinter import ttk, messagebox
root = Tk()
root.option_add("*tearOff", FALSE)
root.title("Графический калькулятор")
root.geometry("500x500")
root.minsize(500, 500)

canvas = Canvas(bg="white", width=400, height=230)
output = ttk.Label(root, text="")


def help():
    """ Справка """
    messagebox.showinfo("Справка", 'Создатель этого "шедевра" Сакулин Иван Михайлович, дата изготовления 23.04.2025, срок годности 2 дня.')


def draw(w, h):
    """ Рисует прямоугольник """
    cw, ch = canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    canvas.delete("all")
    canvas.create_rectangle(
        (cw/2 - w/2),
        (ch/2 - h/2),
        (cw/2 + w/2),
        (ch/2 + h/2),
        fill="#80CBC4", outline="#004D40"
        )
    
def calculate(a=None, b=None):
    """ Рассчёты и вывод """
    try:
        if a is not None:
            a, b = float(a), float(arg2.get())
        elif b is not None:
            a, b = float(arg1.get()), float(b)
        else:
            a, b = float(arg1.get()), float(arg2.get())
    except ValueError:
        output.configure(text="Введите данные")
        print("ERR", arg1.get(), arg2.get())
        return
    print("Калькулируем", a, b)
    if mode.get() == "rect":
        draw(a, b)
        s = ""
        if check[4].get():
            s += f"Периметр P = {2*(a+b):.5f}\n"
        if check[5].get():
            s += f"Площадь S = {a*b:.5f}\n"
        if s == "":
            s = "Не выбрано, что нужно посчитать"
        else:
            s = s[:-2]
        output.configure(text=s)
    elif mode.get() == "calc":
        s = ""
        if check[0].get():
            s += f"Сумма a+b = {a+b:.5f}\n"
        if check[1].get():
            s += f"Разность a-b = {a-b:.5f}\n"
        if check[2].get():
            s += f"Произведение a*b = {a*b:.5f}\n"
        if check[3].get():
            try:
                s += f"Частное a/b = {a/b:.5f}\n"
            except ZeroDivisionError:
                s += "На 0 делить нельзя!\n"
        if s == "":
            s = "Не выбрано, что нужно посчитать"
        else:
            s = s[:-2]
        output.configure(text=s)

def validate(newval):
    """ Проверка текста из ввода"""
    if newval == "-" or newval == "":
        return True
    try:
        v = float(newval)
        if mode.get() == "rect":
            return v > 0
        return True
    except:
        return False

def callback(newval, state=0):
    """ Проверка формы ввода при вводе """
    print("State =", state)
    if not validate(newval):
        return False
    print("Newval =", newval)
    if state == "1":
        calculate(a=newval)
    elif state == "2":
        calculate(b=newval)
    else:
        calculate()
    return True
    
def update():
    """ Проверка форм при нажатиях """
    if not callback(arg1.get()):
        first_entry.delete(0, END)
    if not callback(arg2.get()):
        second_entry.delete(0, END)


def swap():
    """ Меняет местами текст в формах """
    f, s = first_entry.get(), second_entry.get()
    first_entry.delete(0, END)
    second_entry.delete(0, END)
    first_entry.insert(0, s)
    second_entry.insert(0, f)
    
def clear():
    """ Очищает поля """
    first_entry.delete(0, END)
    second_entry.delete(0, END)
    

def show_calc():
    """ Показать объекты калькулятора """
    update()
    rect_frame.pack_forget()
    calc_frame.pack()
    canvas.pack_forget()

def show_rect():
    """ Показать объекты прямоугулятора """
    update()
    calc_frame.pack_forget()
    rect_frame.pack()
    canvas.pack()


"""    Настройки рассчётов    """ 

calc_frame = ttk.Frame(root)
rect_frame = ttk.Frame(root)

check = [BooleanVar(calc_frame, 1), BooleanVar(calc_frame, 1), BooleanVar(calc_frame, 1), 
         BooleanVar(calc_frame, 1), BooleanVar(rect_frame, 1), BooleanVar(rect_frame, 1)]

sum_chb = ttk.Checkbutton(calc_frame, text='сумма', variable=check[0], command=update)
sub_chb = ttk.Checkbutton(calc_frame, text='разность', variable=check[1], command=update)
prod_chb = ttk.Checkbutton(calc_frame, text='произведение', variable=check[2], command=update)
div_chb = ttk.Checkbutton(calc_frame, text='частное', variable=check[3], command=update)

rect_check = [BooleanVar(rect_frame, 0), BooleanVar(rect_frame, 0)]
perimetr_chb = ttk.Checkbutton(rect_frame, text='периметр', variable=check[4], command=update)
square_chb = ttk.Checkbutton(rect_frame, text='площадь', variable=check[5], command=update)

"""    Выбор режима    """ 

mode = StringVar(root, "calc")
calc_rdb = ttk.Radiobutton(root, text='калькулятор', variable=mode, value="calc", command=show_calc)
rect_rdb = ttk.Radiobutton(root, text='прямоугольник', variable=mode, value="rect", command=show_rect)

"""    Ввод текста    """ 

arg1, arg2 = StringVar(root), StringVar(root)
first_entry = ttk.Entry(root, textvariable=arg1, validate="all", validatecommand=(root.register(callback), "%P", 1))
second_entry = ttk.Entry(root, textvariable=arg2, validate="all", validatecommand=(root.register(callback), "%P", 2))

"""    Кнопки    """ 

swap_btn = ttk.Button(root, text="Поменять местами аргументы", command=swap)
clear_btn = ttk.Button(root, text="Очистить форму", command=clear)
exit_btn = ttk.Button(root, text="Выход", command=exit)

""" Расположение кнопок """

calc_rdb.pack()
rect_rdb.pack()

Label(text="Первый аргумент a").pack()
first_entry.pack()
Label(text="Второй аргумент b").pack()
second_entry.pack()

swap_btn.pack()
clear_btn.pack()
exit_btn.pack()

output.pack()


sum_chb.pack()
sub_chb.pack()
prod_chb.pack()
div_chb.pack()
calc_frame.pack()
perimetr_chb.pack()
square_chb.pack()
rect_frame.pack()
show_calc()

"""    МЕНЮ    """ 

file_menu = Menu()
file_menu.add_command(label="Выход", command=exit)

operation_menu = Menu()
operation_menu.add_command(label="Очистить данные", command=clear)
operation_menu.add_separator()
operation_menu.add_checkbutton(label='сумма', variable=check[0], command=update)
operation_menu.add_checkbutton(label='разность', variable=check[1], command=update)
operation_menu.add_checkbutton(label='произведение', variable=check[2], command=update)
operation_menu.add_checkbutton(label='частное', variable=check[3], command=update)
operation_menu.add_separator()
operation_menu.add_checkbutton(label='периметр', variable=check[4], command=update)
operation_menu.add_checkbutton(label='площадь', variable=check[5], command=update)

main_menu = Menu()
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Операции", menu=operation_menu)
main_menu.add_cascade(label="Справка", command=help)

root.config(menu=main_menu)

if __name__ == "__main__":
    root.mainloop()