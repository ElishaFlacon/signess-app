import os
import cv2
import csv


class ClassificationService():
    def classificate(network, autograph, path_to_dataset, path_to_picture, path_to_csv="./result/persons.csv"):
        temp_path = "./temp.png"

        picture = autograph.get_clear_autograph(path_to_picture)
        cv2.imwrite(temp_path, picture)

        classify = network.classify(temp_path, path_to_dataset)
        os.remove(temp_path)

        csv_result = []
        with open(path_to_csv) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                csv_result.append(row)

        def sort(item):
            return item[1]

        result = sorted(
            zip(csv_result, classify[0]),
            key=sort,
            reverse=True
        )[:3]

        return result
