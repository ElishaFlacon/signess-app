from sklearn.metrics import roc_auc_score


class ModelService():
    def load(network, path):
        network.load(path)

    def save(network, path):
        network.save(f"{path}/model")

    def train(network, dataset, epochs):
        network.train(dataset, epochs)

    def blunt(network):
        network.blunt()

    def accuracy(network, dataset):
        predicts = network.predict(dataset)
        roc_auc = roc_auc_score(
            y_true=dataset.target,
            y_score=predicts.predict,
            multi_class="ovo"
        )
        return roc_auc
