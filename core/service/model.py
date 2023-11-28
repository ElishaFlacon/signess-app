class ModelService():
    def load(network, path):
        network.load(path)

    def save(network, path):
        network.save(f"{path}/model")

    def train(network, dataset, epochs):
        network.train(dataset, epochs)
