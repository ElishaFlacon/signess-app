import numpy
import sklearn.metrics as sm
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

    def metrics(network, dataset):
        predicts = network.predict(dataset)
        predicts_list = predicts.predict.tolist()

        labels = dataset.class_labels

        y_true = dataset.target
        y_pred = []
        for predict in predicts_list:
            y = predict.index(max(predict))
            y_pred.append(str(y))

        accuracy = sm.accuracy_score(
            y_true=y_true,
            y_pred=y_pred
        )

        precision = sm.precision_score(
            y_true=y_true,
            y_pred=y_pred,
            labels=labels,
            average="micro"
        )

        recall = sm.recall_score(
            y_true=y_true,
            y_pred=y_pred,
            labels=labels,
            average="micro"
        )

        roc_auc = sm.roc_auc_score(
            y_true=y_true,
            y_score=predicts_list,
            multi_class="ovo"
        )

        fpr, tpr, _ = sm.roc_curve(
            y_true=y_true,
            y_score=predicts_list
        )
        roc_auc_curve = sm.auc(fpr, tpr)

        confusion_matrix = sm.confusion_matrix(
            y_true=y_true,
            y_pred=y_pred
        )
        confusion_matrix = numpy.flip(confusion_matrix)

        drop_count = 0
        drop_path = "./drops.csv"
        open(drop_path, "w")

        files = csv_to_array("./result/filenames.csv")
        files_count = len(files)

        for i, predictArr in enumerate(predicts_list):
            predictIndex = max(enumerate(predictArr), key=lambda x: x[1])[0]
            predict = labels[predictIndex]
            target = y_true[i]

            if predict != target:
                drop_count += 1
                with open(drop_path, 'a') as file:
                    file.write(
                        f'{files[i][0]},predict:{predict},expected:{target}\n'
                    )

        return {
            roc_auc,
            accuracy,
            precision,
            recall,
            confusion_matrix,
            roc_auc_curve,
            fpr,
            tpr,
            files_count,
            drop_count,
            labels
        }
