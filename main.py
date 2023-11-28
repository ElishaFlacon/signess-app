import sv_ttk
import tkinter as tk
from tkinter import ttk

from config import Config
from core.comands import Comands
from core.components import Components


def run():
    root = tk.Tk()

    # настройка стилей
    ttk.Combobox(root, background="#fff")
    sv_ttk.set_theme("dark")

    App(root)
    root.mainloop()


class App(Config, Comands, Components):
    def __init__(self, root):
        Config.__init__(self, root)
        Components.__init__(self, root)


if __name__ == "__main__":
    run()
