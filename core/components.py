from tkinter import ttk


class Components():
    """

    Класс отвечает за отрисовку UI

    """

    def __init__(self, root):
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

        self.btn_train_blunt = ttk.Button(
            master=root,
            text="Сбросить обучение",
            command=self.blunt_model,
        )

        self.btn_accuracy = ttk.Button(
            master=root,
            text="Проверить точность",
            command=self.accuracy_model,
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

        self.label_dataset = ttk.Label(
            master=root,
            text="Нет датасета",
            foreground="red",
            anchor="center"
        )

        self.label_model = ttk.Label(
            master=root,
            text="Модель не обучена",
            foreground="red",
            anchor="center"
        )

        self.entry_epochs = ttk.Entry(master=root)

    def __render_components(self):
        self.btn_load_dataset.place(x=30, y=30, width=200, height=40)
        self.btn_generate_dataset.place(x=30, y=80, width=200, height=40)
        self.btn_accuracy.place(x=30, y=130, width=200, height=40)

        self.btn_load_model.place(x=240, y=30, width=200, height=40)
        self.btn_save_model.place(x=240, y=80, width=200, height=40)
        self.btn_train_blunt.place(x=240, y=130, width=200, height=40)

        self.btn_train_model.place(x=30, y=180, width=410, height=40)
        self.btn_classification.place(x=30, y=230, width=410, height=40)

        self.label_dataset.place(x=450, y=30, width=210, height=40)
        self.label_model.place(x=450, y=80, width=210, height=40)
        self.entry_epochs.place(x=450, y=130, width=210, height=40)
