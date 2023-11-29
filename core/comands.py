from threading import Thread
import tkinter.filedialog as tkFile
from core.service.model import ModelService
from core.service.dataset import DatasetService
from core.service.classification import ClassificationService
from core.utils import show_info, show_error, check_path, check_dataset


class Comands():
    """

    В этом классе находится все основные команды

    Логика для команд находится в сервисах

    """

    def load_model(self):
        path = tkFile.askdirectory()
        if not check_path(path):
            return

        try:
            ModelService.load(self.network, path)
            self.label_model.configure(
                text="Модель готова",
                foreground="lime"
            )
        except:
            show_error()

    def save_model(self):
        path = tkFile.askdirectory()
        if not check_path(path):
            return

        try:
            ModelService.save(self.network, path)
        except:
            show_error()

    # TODO ЭПОХИ
    def train_model(self):
        if not check_dataset(self.dataset):
            return

        def train():
            ModelService.train(self.network, self.dataset, 3)
            self.label_model.configure(
                text="Модель готова",
                foreground="lime"
            )
            show_info("Модель обучена!")

        try:
            self.label_model.configure(
                text="Модель обучается...",
                foreground="orange"
            )

            th_train = Thread(target=train)
            th_train.start()

        except:
            self.label_model.configure(
                text="Нет обученной модели",
                foreground="red"
            )
            show_error()

    def load_dataset(self):
        filetypes = (("Датасет", "*.npz"),)
        path = tkFile.askopenfilename(
            title="Загрузка npz датасета",
            filetypes=filetypes
        )

        if not check_path(path):
            return

        try:
            dataset = DatasetService.load(self.network, path)
            self.path_to_dataset = path
            self.dataset = dataset
            self.label_dataset.configure(
                text="Датасет загружен",
                foreground="lime"
            )
            show_info("Датасет загружен!")
        except:
            show_error()

    def generate_dataset(self):
        path = tkFile.askdirectory()
        if not check_path(path):
            return

        try:
            dataset = DatasetService.generate(
                self.network,
                path,
                self.autograph,
                self.document
            )
            self.path_to_dataset = path
            self.dataset = dataset
            self.label_dataset.configure(
                text="Датасет загружен",
                foreground="lime"
            )
            show_info("Датасет загружен!")
        except:
            show_error()

    def classification(self):
        if not check_dataset(self.dataset):
            return
        if not check_dataset(self.path_to_dataset):
            return

        filetypes = (("Изображение", "*.png *.jpg *.jpeg *.pdf"),)
        path = tkFile.askopenfilename(
            title="Открыть файл",
            filetypes=filetypes
        )

        if not check_path(path):
            return

        # filetype = path.split('.')[-1]
        # if(filetype == "pdf"):
        #     with fitz.open(path) as pdf:
        #         page = pdf.load_page(0)
        #         pix = page.get_pixmap()
        #         pix.save(path)

        try:
            classify = ClassificationService.classificate(
                self.network,
                self.autograph,
                self.path_to_dataset,
                path
            )
            show_info(str(classify))
        except:
            show_error()
