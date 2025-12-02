import tkinter as tk

FONT_H2 = ('Helvetica', 12, 'bold')
FONT_NORMAL = ('Helvetica', 10)
FONT_MONO = ('Courier', 10)

def make_frame(master, title):
    return tk.LabelFrame(master, text=title, font=FONT_H2, padx=10, pady=10)
