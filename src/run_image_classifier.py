import sys
import os
import numpy as np

from config.stage import ConfigStage
from extract.stage import ExtractStage
from model.stage import ModelStage
from preprocess.stage import PreprocessStage


def common_resources():
    return os.path.abspath(os.path.join(__file__, "../..", "resources"))


def run(config_path):
    config = ConfigStage().run(config_path)

    for action in config["actions"]:
        images, labels = ExtractStage().run(config, action)
        images, labels = PreprocessStage().run(images, labels, config, action)
        if action == "train":
            model = ModelStage().run(images, labels, config)
        else:
            model = ModelStage().create_model(config)
            model.load_weights(common_resources() + "/" + config["model_path"])
        predicted_labels = model.predict(images)
        predictions = np.argmax(predicted_labels, axis=1)
        print(predictions)
    return predictions


if __name__ == '__main__':
    run(config_path=sys.argv[1])
