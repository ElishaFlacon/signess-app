import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


class Components():
    """

    Класс отвечает за отрисовку UI

    """

    def __init__(self, root):
        self.__bullshit(root)
        self.__generate_components(root)
        self.__render_components()

    def __generate_components(self, root):
        self.btn_load_model = ttk.Button(
            master=root,
            text="Загрузить модель",
            command=self.load_model,
        )

        self.btn_save_model = ttk.Button(
            master=root,
            text="Сохранить модель",
            command=self.save_model,
        )

        self.btn_train_model = ttk.Button(
            master=root,
            text="Обучить модель",
            command=self.train_model,
        )

        self.btn_generate_dataset = ttk.Button(
            master=root,
            text="Создать датасет",
            command=self.generate_dataset,
        )

        self.btn_load_dataset = ttk.Button(
            master=root,
            text="Загрузить датасет",
            command=self.load_dataset,
        )

        self.btn_classification = ttk.Button(
            master=root,
            text="Классификация",
            command=self.classification,
        )

    def __render_components(self):
        self.btn_load_dataset.place(x=180, y=20, width=150, height=40)
        self.btn_generate_dataset.place(x=180, y=70, width=150, height=40)
        self.btn_load_model.place(x=180, y=120, width=150, height=40)
        self.btn_save_model.place(x=180, y=170, width=150, height=40)
        self.btn_train_model.place(x=180, y=220, width=150, height=40)
        self.btn_classification.place(x=180, y=270, width=150, height=40)

    # отрефакторить (нет)
    def __bullshit(self, root):
        GListBox_620 = tk.Listbox(root)
        GListBox_620["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_620["font"] = ft
        GListBox_620["fg"] = "#333333"
        GListBox_620["justify"] = "center"
        GListBox_620.place(x=10, y=50, width=150, height=100)

        GListBox_547 = tk.Listbox(root)
        GListBox_547["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_547["font"] = ft
        GListBox_547["fg"] = "#333333"
        GListBox_547["justify"] = "center"
        GListBox_547.place(x=350, y=10, width=230, height=200)

        GListBox_143 = tk.Listbox(root)
        GListBox_143["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_143["font"] = ft
        GListBox_143["fg"] = "#333333"
        GListBox_143["justify"] = "center"
        GListBox_143.place(x=350, y=220, width=230, height=30)

        GCheckBox_258 = tk.Checkbutton(root)
        GCheckBox_258["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_258["font"] = ft
        GCheckBox_258["fg"] = "#333333"
        GCheckBox_258["justify"] = "center"
        GCheckBox_258["text"] = "Датасет"
        GCheckBox_258["relief"] = "flat"
        GCheckBox_258.place(x=10, y=60, width=150, height=40)
        GCheckBox_258["offvalue"] = "0"
        GCheckBox_258["onvalue"] = "1"

        GCheckBox_979 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_979["font"] = ft
        GCheckBox_979["fg"] = "#333333"
        GCheckBox_979["justify"] = "center"
        GCheckBox_979["text"] = "Модель"
        GCheckBox_979.place(x=10, y=100, width=150, height=40)
        GCheckBox_979["offvalue"] = "0"
        GCheckBox_979["onvalue"] = "1"
