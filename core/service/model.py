import numpy
import sklearn.metrics as sm
# from sklearn.preprocessing import label_binarize
from core.utils import csv_to_array


class ModelService():
    def load(self, network, path):
        network.load(path)

    def save(self,network, path):
        network.save(f"{path}/model")

    def train(self,network, dataset, epochs):
        network.train(dataset, epochs)

    def blunt(self,network):
        network.blunt()

    def metrics(self,network, dataset):
        predicts = network.predict(dataset)
        predicts_list = predicts.predict.tolist()

        labels = dataset.class_labels
        n_labels = len(labels.tolist())

        y_true = dataset.target
        y_pred = []
        for predict in predicts_list:
            y_index = predict.index(max(predict))
            y = labels[y_index]
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

        # fpr, tpr, roc_auc_curve = dict(), dict(), dict()
        # for i in range(n_labels):
        #     fpr[i], tpr[i], _ = sm.roc_curve(
        #         y_true=y_true[i],
        #         y_score=predicts_list[i]
        #     )
        #     roc_auc[i] = sm.auc(fpr[i], tpr[i])

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
            predict_index = max(enumerate(predictArr), key=lambda x: x[1])[0]
            predict = labels[predict_index]
            target = y_true[i]

            if predict != target:
                drop_count += 1
                with open(drop_path, 'a') as file:
                    file.write(
                        f'{files[i][0]},predict:{predict},expected:{target}\n'
                    )

        return {
            "roc_auc": roc_auc,
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "confusion_matrix": confusion_matrix,
            # "roc_auc_curve": roc_auc_curve,
            # "fpr": fpr,
            # "tpr": tpr,
            "files_count": files_count,
            "drop_count": drop_count,
            "labels": labels,
            "n_labels": n_labels
        }
