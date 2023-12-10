import tkinter
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from core import constants, get_members
import widgets.basic_widgets
import widgets.window_settings
import pyperclip

window = tkinter.Tk()
widgets.window_settings.main_window_settings(window)

source_dimension_list = []
target_dimension_list = []

# Widgets
source_label = widgets.basic_widgets.default_label('SOURCE CUBE', fg_color=constants.source_label_color)
target_label = widgets.basic_widgets.default_label('TARGET CUBE', fg_color=constants.target_label_color)


def getConstants():
    if source_cube_combobox.get() == 'Select Source Cube' and target_cube_combobox.get() == 'Select Target Cube':
        messagebox.showwarning("Warning", "Please Select Source or Target Cube!")
    else:
        show_widget()
        prolog_text.delete('1.0', tkinter.END)
        prolog_x = constants.prolog(sourceCubeName=source_cube_combobox.get(),
                                    targetCubeName=target_cube_combobox.get(),
                                    sourceCount=len(source_dimension_list), targetCount=len(target_dimension_list),
                                    dimSourceNames=source_dimension_list, dimTargetNames=target_dimension_list,
                                    selected_items_source=selected_items_source,
                                    selected_items_target=selected_items_target)
        prolog_text.insert("1.0", prolog_x)

        epilog_text.delete('1.0', tkinter.END)
        epilog_x = constants.epilog(sourceCubeName=source_cube_combobox.get(),
                                    targetCubeName=target_cube_combobox.get(),
                                    sourceCount=len(source_dimension_list), targetCount=len(target_dimension_list))
        epilog_text.insert("1.0", epilog_x)


def clearConstants():
    prolog_text.delete('1.0', tkinter.END)
    epilog_text.delete('1.0', tkinter.END)


generate_button = tkinter.Button(text='Generate Process',
                                 bg='#000000',
                                 fg='#FFFFFF',
                                 bd=0,
                                 activebackground='#282828',
                                 activeforeground='#FFFFFF',
                                 font=('Calibre', 12),
                                 width=20,
                                 height=2,
                                 command=getConstants)

clear_button = tkinter.Button(text='Clear',
                              bg='#CD3700',
                              fg='#FFFFFF',
                              bd=0,
                              activebackground='#8B2500',
                              activeforeground='#FFFFFF',
                              font=('Calibre', 12),
                              width=10,
                              height=1,
                              command=clearConstants)


def copy_mdx_text(metin):
    pyperclip.copy(metin)


def mdx_button(mdx_window, mdx_text1):
    return tkinter.Button(mdx_window, bg='#000000',
                          fg='#FFFFFF',
                          bd=0,
                          activebackground='#282828',
                          activeforeground='#FFFFFF',
                          font=('Calibre', 12),
                          justify="left",
                          text=mdx_text1,
                          command=lambda mdx_text=mdx_text1: copy_mdx_text(mdx_text))


def open_mdx_form():
    mdx_window = tkinter.Toplevel(window)
    widgets.window_settings.mdx_window_settings(mdx_window)
    mdx8_button = mdx_button(mdx_window, '''MDXX = '{TM1FILTERBYLEVEL({TM1DRILLDOWNMEMBER({['|v_DimSourceNameX|'].['|p_Period|']},ALL,RECURSIVE)},0)}';
SUBSETCREATEBYMDX(v_SubSourceNameX, MDXX, 0);''')
    mdx8_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)
    mdx7_button = mdx_button(mdx_window, '''MDXX = '{TM1FILTERBYLEVEL({TM1DRILLDOWNMEMBER({['|v_DimXName|'].['|p_Period|']},ALL,RECURSIVE)},0)}';
SUBSETCREATEBYMDX(v_SubsXName, MDXX, 0);''')
    mdx7_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)
    mdx6_button = mdx_button(mdx_window, '''MDXX = '{TM1FILTERBYLEVEL({TM1DRILLDOWNMEMBER({['|v_DimSourceNameX|'].[Total X]},ALL,RECURSIVE)},0)}';
SUBSETCREATEBYMDX(v_SubSourceNameX, MDXX, 0);''')
    mdx6_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)
    mdx5_button = mdx_button(mdx_window, '''MDXX = '{TM1FILTERBYLEVEL({TM1DRILLDOWNMEMBER({['|v_DimXName|'].[Total X]},ALL,RECURSIVE)},0)}';
SUBSETCREATEBYMDX(v_SubsXName, MDXX, 0);''')
    mdx5_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)
    mdx4_button = mdx_button(mdx_window, '''MDXX = 'EXCEPT(TM1FILTERBYLEVEL(TM1DRILLDOWNMEMBER({['|v_DimSourceNameX|'].[Total X]}, ALL, RECURSIVE), 0), {['|v_DimSourceNameX|'].[GA/Insurance]})';
SUBSETCREATEBYMDX(v_SubSourceNameX, MDXX, 0);''')
    mdx4_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)
    mdx3_button = mdx_button(mdx_window, '''MDXX = 'EXCEPT(TM1FILTERBYLEVEL(TM1DRILLDOWNMEMBER({['|v_DimXName|'].[Total X]}, ALL, RECURSIVE), 0), {['|v_DimXName|'].[GA/Insurance]})';
SUBSETCREATEBYMDX(v_SubsXName, MDXX, 0);''')
    mdx3_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)
    mdx2_button = mdx_button(mdx_window, '''MDXX = 'EXCEPT(TM1FILTERBYLEVEL(TM1SUBSETALL(['|v_DimSourceNameX|']), 0), {['|v_DimSourceNameX|'].[TRY_Report]})';
SUBSETCREATEBYMDX(v_SubSourceNameX, MDXX, 0);''')
    mdx2_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)
    mdx1_button = mdx_button(mdx_window, '''MDXX = 'EXCEPT(TM1FILTERBYLEVEL(TM1SUBSETALL(['|v_DimXName|']), 0), {['|v_DimXName|'].[TRY_Report]})';
SUBSETCREATEBYMDX(v_DimXName, MDXX, 0);''')
    mdx1_button.pack(pady=10, padx=5, side=tkinter.BOTTOM, anchor=tkinter.NW)


mdx_list_button = tkinter.Button(text='Show MDX List',
                                 bg='#E4850B',
                                 fg='#FFFFFF',
                                 bd=0,
                                 activebackground='#AE7A38',
                                 activeforeground='#FFFFFF',
                                 font=('Calibre', 12),
                                 command=open_mdx_form)


def copy_prolog():
    window.clipboard_clear()
    window.clipboard_append(prolog_text.get("1.0", "end-1c"))
    window.update()


def copy_epilog():
    window.clipboard_clear()
    window.clipboard_append(epilog_text.get("1.0", "end-1c"))
    window.update()


prolog_copy_button = tkinter.Button(text='Copy Prolog',
                                    bg='#000000',
                                    fg='#FFFFFF',
                                    bd=0,
                                    activebackground='#282828',
                                    activeforeground='#FFFFFF',
                                    font=('Calibre', 12),
                                    width=10,
                                    height=1,
                                    command=copy_prolog)

epilog_copy_button = tkinter.Button(text='Copy Epilog',
                                    bg='#000000',
                                    fg='#FFFFFF',
                                    bd=0,
                                    activebackground='#282828',
                                    activeforeground='#FFFFFF',
                                    font=('Calibre', 12),
                                    width=10,
                                    height=1,
                                    command=copy_epilog)

prolog_text = ScrolledText(window, height=20, width=70, bg=constants.system_theme_color, fg='#FFFFFF', bd=0,
                           insertbackground='white', font=('Arial', 10), highlightthickness=1, borderwidth=0,
                           pady=5, padx=5)
epilog_text = ScrolledText(window, height=10, width=70, bg=constants.system_theme_color, fg='#FFFFFF', bd=0,
                           insertbackground='white', font=('Arial', 10), highlightthickness=1, borderwidth=0,
                           pady=5, padx=5)

source_cube_combobox = widgets.basic_widgets.default_comboBox()
target_cube_combobox = widgets.basic_widgets.default_comboBox()
source_cube_combobox.set('Select Source Cube')
target_cube_combobox.set('Select Target Cube')

source_listbox = tkinter.Listbox(bg=constants.system_theme_color, fg='white', width=30)
target_listbox = tkinter.Listbox(bg=constants.system_theme_color, fg='white', width=30)


def open_element_form(cubeType, selected_item, selected_item_index):
    new_window = tkinter.Toplevel(window)
    widgets.window_settings.element_window_settings(new_window, selected_item)
    fm = tkinter.Frame(new_window, padx=5, pady=5)
    scroll_bar = tkinter.Scrollbar(fm)
    scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    text_area = tkinter.Text(fm, bg=constants.system_theme_color, fg='white')
    text_area.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=3, pady=3)
    text_area.configure(yscrollcommand=scroll_bar.set)
    scroll_bar.configure(command=text_area.yview)
    element_add_button = tkinter.Button(fm, text='Add Elements', bg=constants.system_theme_color,
                                        fg='#FFFFFF',
                                        bd=0,
                                        activebackground='#282828',
                                        activeforeground=constants.system_theme_color,
                                        font=('Calibre', 12), command=new_window.destroy)
    element_add_button.pack(side=tkinter.BOTTOM, anchor=tkinter.NW, padx=3, pady=3)

    fm.pack()
    selected_checkboxes = []
    for item in get_members.get_elements(cubeType=cubeType, dimensionName=selected_item):
        checkboxVar = tkinter.BooleanVar()
        checkbox = tkinter.Checkbutton(text_area, text=item, onvalue=1, offvalue=0,
                                       bg=constants.system_theme_color, fg='#FFFFFF',
                                       selectcolor='#626567', variable=checkboxVar,
                                       command=lambda label_text=item, checkbox_var=checkboxVar: toggle_checkbox_state(
                                           cubeType, selected_item_index, checkbox_var, label_text))
        selected_checkboxes.append(checkbox)
        text_area.window_create('end', window=checkbox)
        text_area.insert('end', '\n')

    text_area.configure(state=tkinter.DISABLED, cursor='')


selected_items_source = []
selected_items_target = []


def toggle_checkbox_state(cubeType, dimensionIndex, checkbox_var, label_text):
    if checkbox_var.get():
        if cubeType == 'Source':
            selected_items_source.append(str(dimensionIndex) + label_text)
            selected_items_source.sort()
        else:
            selected_items_target.append(str(dimensionIndex) + label_text)
            selected_items_source.sort()
    else:
        if cubeType == 'Source':
            selected_items_source.remove(str(dimensionIndex) + label_text)
            selected_items_target.sort()
        else:
            selected_items_target.remove(str(dimensionIndex) + label_text)
            selected_items_target.sort()


def source_listbox_selector(event):
    selected_indices = source_listbox.curselection()
    if selected_indices:
        selected_item = source_listbox.get(selected_indices[0])
        selected_item_index = source_listbox.index(selected_indices)
        open_element_form('Source', selected_item, selected_item_index)
    else:
        print("No item selected in source listbox")


def target_listbox_selector(event):
    selected_indices = target_listbox.curselection()
    if selected_indices:
        selected_item = target_listbox.get(selected_indices[0])
        selected_item_index = target_listbox.index(selected_indices)
        open_element_form('Target', selected_item, selected_item_index)
    else:
        print("No item selected in target listbox")


def source_cube_selector(event):
    source_dimension_list.clear()
    selected_items_source.clear()
    dimension_list = get_members.get_dimensions(cubeType='Source', cubeName=source_cube_combobox.get())
    source_listbox.delete(0, tkinter.END)
    source_listbox.grid(row=2, column=0, padx=1, pady=1)
    for item in dimension_list:
        source_listbox.insert(tkinter.END, item)
        source_dimension_list.append(item)


def target_cube_selector(event):
    target_dimension_list.clear()
    selected_items_target.clear()
    dimension_list = get_members.get_dimensions(cubeType='Target', cubeName=target_cube_combobox.get())
    target_listbox.delete(0, tkinter.END)
    target_listbox.grid(row=2, column=2, padx=1, pady=1)
    for item in dimension_list:
        target_listbox.insert(tkinter.END, item)
        target_dimension_list.append(item)


source_cube_combobox.bind("<<ComboboxSelected>>", source_cube_selector)
target_cube_combobox.bind("<<ComboboxSelected>>", target_cube_selector)
source_listbox.bind("<<ListboxSelect>>", source_listbox_selector)
target_listbox.bind("<<ListboxSelect>>", target_listbox_selector)

# Hizalamalar
source_label.grid(row=0, column=0)
target_label.grid(row=0, column=2)
source_cube_combobox.grid(row=1, column=0)
target_cube_combobox.grid(row=1, column=2)
generate_button.grid(row=0, column=1)
prolog_copy_button.grid(row=3, column=1, padx=5, pady=5)
prolog_text.grid(row=5, column=1)
epilog_copy_button.grid(row=6, column=1, padx=5, pady=5)
epilog_text.grid(row=8, column=1)


def show_widget():
    clear_button.grid(row=1, column=1, padx=5, pady=5)
    mdx_list_button.grid(row=2, column=1)


window.mainloop()
