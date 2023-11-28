import os
import cv2


class ClassificationService():
    def classificate(network, autograph, path_to_dataset, path_to_picture):
        temp_path = "./temp.png"

        picture = autograph.get_clear_autograph(path_to_picture)
        cv2.imwrite(temp_path, picture)

        classify = network.classify(temp_path, path_to_dataset)
        os.remove(temp_path)

        return classify
