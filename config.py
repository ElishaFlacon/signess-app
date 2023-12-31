from signess.network import FedotCNN

from inskrib.autograph import Autograph
from inskrib.documents import Document


title = "Signess App"

width = 680
height = 350

autograph = Autograph(size=(380, 380))
document = Document()
network = FedotCNN()


class Config():
    def __init__(self, root):
        self.autograph = autograph
        self.document = document

        self.network = network
        self.dataset = None
        self.path_to_dataset = None

        self.epochs_count = 5

        root.title(title)
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()

        alignstr = '%dx%d+%d+%d' % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2
        )

        root.geometry(alignstr)
        root.resizable(width=False, height=False)
