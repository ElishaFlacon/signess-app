import csv
import tkinter.messagebox as tkMb
from matplotlib import pyplot as plt
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


# оставлю так, вряд-ли пригодится
# def check_model_training(network):
#     if network.is_fitted:
#         return True
#     show_error("Модель не обучена!")


def csv_to_array(path_to_csv: str):
    csv_result = []
    with open(path_to_csv) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_result.append(row)

    return csv_result


def show_error(message="Произошла критическая ошибка!"):
    tkMb.showerror("Ошибка!", message)


def show_info(message="Отлично!"):
    tkMb.showinfo("Информация", message)


def roc_auc_plot(fpr, tpr, roc_auc):
    plt.plot(
        fpr,
        tpr,
        color='darkorange',
        label=f'ROC кривая (area = {roc_auc:.2f})'
    )
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Пример ROC-кривой')
    plt.legend(loc="lower right")
    plt.show()