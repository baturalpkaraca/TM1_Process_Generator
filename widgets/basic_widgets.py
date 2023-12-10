import tkinter
from tkinter import ttk
from core import constants, get_members


def default_label(name, fg_color):
    return tkinter.Label(text=name, fg=fg_color, bg=constants.system_theme_color,
                         font=('Calibre', 18, 'bold'))


def default_comboBox():
    return ttk.Combobox(state='readonly', font=('Arial', 10),
                        values=get_members.get_cubes(),
                        width=30,
                        height=30)


def default_dimension_button(name, bg, fg):
    return tkinter.Button(text=name,
                          bg=bg,
                          fg=fg,
                          bd=0,
                          activebackground='#282828',
                          activeforeground='#FFFFFF',
                          font=('Calibre', 12, 'bold'),
                          width=20,
                          height=2)
