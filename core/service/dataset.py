from core.utils import create_dataset


class DatasetService():
    def load(network, path):
        dataset = network.load_dataset(path)
        return dataset

    def generate(network, path, autograph, document):
        path_to_dataset = create_dataset(path, autograph, document)
        dataset = DatasetService.load(network, path_to_dataset)
        return dataset
