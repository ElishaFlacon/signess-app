import time
import fitz
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
        show_info(
            "Загрузка модели работает только с версией Fedot >= 0.7.3"
        )

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

    def train_model(self):
        if not check_dataset(self.dataset):
            return

        def train():
            start_time = time.time()
            ModelService.train(self.network, self.dataset, self.epochs_count)
            self.label_model.configure(
                text=f"Модель готова",
                foreground="lime"
            )
            show_info(f"Модель обучена!\nВремя обучения модели {time.time() - start_time:.3f} секунд")

        try:
            self.label_model.configure(
                text="Модель обучается...",
                foreground="orange"
            )

            thread = Thread(target=train)
            thread.start()
        except:
            self.label_model.configure(
                text="Модель не обучена",
                foreground="red"
            )
            show_error()

    def blunt_model(self):
        try:
            ModelService.blunt(self.network)
            self.label_model.configure(
                text="Модель не обучена",
                foreground="red"
            )
            show_info("Модель сбросила обучение!")
        except:
            show_error()

    def accuracy_model(self):
        filetypes = (("Датасет", "*.npz"),)
        path = tkFile.askopenfilename(
            title="Загрузка npz датасета",
            filetypes=filetypes
        )

        if not check_path(path):
            return

        def accuracy():
            dataset = DatasetService.load(self.network, path)
            (roc_auc, files_count, drop_count) = ModelService.accuracy(
                self.network, dataset)
            show_info(
                f"ROG AUC модели: {(roc_auc * 100):.3f}%\n\nКоличество ошибочных распознавания {drop_count} из {files_count}"
            )

        try:
            thread = Thread(target=accuracy)
            thread.start()
        except:
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

        def generate():
            path_to_dataset = DatasetService.generate(
                path,
                self.autograph,
                self.document
            )
            self.path_to_dataset = path_to_dataset

            dataset = DatasetService.load(self.network, path_to_dataset)
            self.dataset = dataset

            self.label_dataset.configure(
                text="Датасет загружен",
                foreground="lime"
            )
            show_info("Датасет загружен!")

        try:
            thread = Thread(target=generate)
            thread.start()
            show_info("Датасет генерируется...")
        except:
            show_error()

    def classification(self):
        if not check_dataset(self.dataset):
            return
        if not check_dataset(self.path_to_dataset):
            return

        filetypes = (("Файл", "*.png *.jpg *.jpeg *.bmp *.pdf"),)
        path = tkFile.askopenfilename(
            title="Открыть файл",
            filetypes=filetypes
        )

        if not check_path(path):
            return

        filetype = path.split('.')[-1]
        if (filetype == "pdf"):
            with fitz.open(path) as pdf:
                path = "./temp.png"
                page = pdf.load_page(0)
                pix = page.get_pixmap()
                pix.save(path)

        try:
            classify = ClassificationService.classificate(
                self.network,
                self.autograph,
                self.path_to_dataset,
                path
            )

            result = ""
            for item in classify:
                result += f"{item[0][0]}: {item[1]*100}% \n"

            person = f"{classify[0][0][0]}: {classify[0][1]*100}%"
            self.label_result.configure(text=person)

            show_info(result)
        except:
            show_error()

    def epochs(self):
        new_epochs_count = self.entry_epochs.get()
        self.entry_epochs.delete(0, 9999)

        try:
            new_epochs_count = int(new_epochs_count)
        except ValueError:
            show_error("Нужно ввести число!")
            return

        new_epochs_count = abs(new_epochs_count)

        if (new_epochs_count == 0):
            new_epochs_count = 1

        self.label_epochs.configure(
            text=f"Количество эпох: {new_epochs_count}"
        )

        self.epochs_count = new_epochs_count
