import os
import cv2
from core.utils import csv_to_array


class ClassificationService():
    @staticmethod
    def classificate(network, autograph, path_to_dataset, path_to_picture, path_to_csv="./result/persons.csv"):
        temp_path = "./temp.png"

        picture = autograph.get_clear_autograph(path_to_picture)
        cv2.imwrite(temp_path, picture)

        classify = network.classify(temp_path, path_to_dataset)
        os.remove(temp_path)

        persons = csv_to_array(path_to_csv)

        def sort(item):
            return item[1]

        result = sorted(
            zip(persons, classify[0]),
            key=sort,
            reverse=True
        )[:3]

        return result
