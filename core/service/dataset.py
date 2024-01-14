from core.utils import create_dataset


class DatasetService():
    @staticmethod
    def load(network, path):
        dataset = network.load_dataset(path)
        return dataset
    
    @staticmethod
    def generate(path, autograph, document):
        path_to_dataset = create_dataset(path, autograph, document)
        return path_to_dataset
