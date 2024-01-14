from core.utils import create_dataset


class DatasetService():
    def load(self, network, path):
        dataset = network.load_dataset(path)
        return dataset

    def generate(self, path, autograph, document):
        path_to_dataset = create_dataset(path, autograph, document)
        return path_to_dataset
