import sv_ttk
import tkinter as tk
from config import Config
from core.comands import Comands
from core.components import Components


def run():
    root = tk.Tk()
    sv_ttk.set_theme("dark", root)
    App(root)
    root.mainloop()


class App(Config, Comands, Components):
    def __init__(self, root):
        Config.__init__(self, root)
        Components.__init__(self, root)


if __name__ == "__main__":
    run()
