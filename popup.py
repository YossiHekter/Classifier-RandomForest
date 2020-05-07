import tkinter as tk
from tkinter import ttk


def popup_output(dataset):
    # Creating tkinter window
    window = tk.Tk()
    window.title("Classifier results")
    window.resizable(width=1, height=1)

    # Using treeview widget
    treev = ttk.Treeview(window, selectmode='browse')

    # Calling pack method w.r.to treeview
    treev.pack(side='right')

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(window,
                               orient="vertical",
                               command=treev.yview)

    # Calling pack method w.r.to verical
    # scrollbar
    verscrlbar.pack(side='right', fill='x')

    # Configuring treeview
    treev.configure(xscrollcommand=verscrlbar.set)

    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=90, anchor='center')
    treev.column("2", width=90, anchor='center')
    treev.column("3", width=90, anchor='center')
    treev.column("4", width=90, anchor='center')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="DogID")
    treev.heading("2", text="Guide dog")
    treev.heading("3", text="Disabled")
    treev.heading("4", text="Traumatized")

    for index in range(len(dataset)-1):
        treev.insert("", 'end', text="L1",
                     values=(dataset["dogID"][index], dataset["predict a"][index],
                             dataset["predict b"][index], dataset["predict c"][index]))


def popup_msg(msg):
    popup = tk.Tk()
    popup.geometry("250x90")
    popup.wm_title("Error!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    b1 = ttk.Button(popup, text="Ok", command=popup.destroy)
    b1.pack()
    popup.mainloop()


def popup_format_error(msg):
    popup = tk.Tk()
    popup.geometry("350x150")
    popup.wm_title("Error!")
    if msg == "train":
        message = "Format error!\n" \
                  "Your excel file should have 29 columns\n" \
                  "Dog number, dog name, 24 attributes and classification\n" \
                  "You need to add the classification yourself\n" \
                  "After the dog finished his training"
    else:
        message = "Format error!\n" \
                  "Your excel file should have 28 columns\n" \
                  "Dog number, dog name, 24 attributes"
    label = ttk.Label(popup, text=message)
    label.pack(side="top", fill="x", pady=10)
    b1 = ttk.Button(popup, text="Ok", command=popup.destroy)
    b1.pack(side="bottom")
    popup.mainloop()


def model_accuracy(msg):
    popup = tk.Tk()
    popup.geometry("250x90")
    popup.wm_title("Model accuracy!")
    label = ttk.Label(popup, text="The model accuracy is: " + msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Ok", command=popup.destroy)
    B1.pack()
    popup.mainloop()
