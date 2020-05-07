from controller import train_model, classifier_function

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()


w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+351+147")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Dog classifier")
        top.configure(background="#d7d7d7")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#7f7f7f")

        self.Button1 = tk.Button(top, command=train_model)
        self.Button1.place(relx=0.25, rely=0.689, height=24, width=83)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Train a model''')

        self.Button2 = tk.Button(top, command=classifier_function)
        self.Button2.place(relx=0.6, rely=0.689, height=24, width=58)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Classifier''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.033, rely=0.156, height=71, width=564)
        self.Label1.configure(activebackground="#d7d7d7")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d7d7d7")
        self.Label1.configure(compound='center')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 22 -weight bold")
        self.Label1.configure(foreground="#000080")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Welcome to the dog classifier!''')


if __name__ == '__main__':
    vp_start_gui()