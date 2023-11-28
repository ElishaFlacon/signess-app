import tkinter.messagebox as tkMb
from signess.dataset import Dataset


def create_dataset(path, autograph, document):
    dataset = Dataset(autograph, document)
    path_to_dataset = dataset.generate(path)
    return path_to_dataset


def check_path(path):
    if path:
        return True
    show_error("Нет пути! (No way!)")


def check_dataset(dataset):
    if dataset:
        return True
    show_error("Нет датасета!")


def show_error(message="Произошла критическая ошибка!"):
    tkMb.showerror("Ошибка!", message)


def show_info(message="Отлично!"):
    tkMb.showinfo("Информация", message)
