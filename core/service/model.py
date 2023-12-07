from sklearn.metrics import roc_auc_score
from core.utils import csv_to_array


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

        drop_count = 0
        drop_path = "./drops.csv"
        open(drop_path, "w")

        files = csv_to_array("./result/filenames.csv")
        files_count = len(files)

        labels = dataset.class_labels
        for i, predictArr in enumerate(predicts.predict):
            predictIndex = max(enumerate(predictArr), key=lambda x: x[1])[0]
            predict = labels[predictIndex]
            target = dataset.target[i]

            if predict != target:
                drop_count += 1
                with open(drop_path, 'a') as file:
                    file.write(
                        f'{files[i][0]},predict:{predict},expected:{target}\n'
                    )

        return (roc_auc, files_count, drop_count)
