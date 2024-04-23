# This file contains the samples codes for "Graphical User Interface" section.

#%% Graphical User Interface (2)
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title('My GUI')
window.geometry('320x200')
lbl = ttk.Label(window, text='Hello world!').grid()
Btn = ttk.Button(window, text='Close', 	command=window.destroy).grid()
window.mainloop()

# %% Graphical User Interface (4)
import easygui as gui
gui.msgbox(msg="Hello world!", title="Hello")
