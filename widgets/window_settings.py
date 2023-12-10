from core import constants


def main_window_settings(window):
    window.configure(bg=constants.system_theme_color, padx=10, pady=10)
    window.title('TM1 Process Generator')
    window.resizable(False, False)
    window.option_add('*TCombobox*Listbox*Background', constants.system_theme_color)
    window.option_add('*TCombobox*Listbox*Foreground', '#FFFFFF')
    window.option_add('*TCombobox*Listbox*selectBackground', '#626567')
    window.option_add('*TCombobox*Listbox*selectForeground', '#FFFFFF')


def element_window_settings(new_window, selected_item):
    new_window.attributes('-topmost', 1)
    new_window.focus()
    new_window.bind("<Key-Escape>", lambda event: new_window.destroy())
    new_window.grab_set()
    new_window.title(f"Dimension: {selected_item}")
    new_window.configure(bg=constants.system_theme_color)
    # new_window.iconbitmap('./assets/icon_min.ico')
    # new_window.geometry('600x400+800+300')
    new_window.resizable(False, False)


def mdx_window_settings(mdx_window):
    mdx_window.attributes('-topmost', 1)
    mdx_window.focus()
    mdx_window.bind("<Key-Escape>", lambda event: mdx_window.destroy())
    mdx_window.grab_set()
    mdx_window.title("MDX List")
    mdx_window.configure(bg=constants.system_theme_color)
    mdx_window.resizable(False, False)
