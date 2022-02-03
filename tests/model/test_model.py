import os

import pytest
import tensorflow as tf

from config.stage import ConfigStage
from extract.stage import ExtractStage
from model.stage import ModelStage
from preprocess.stage import PreprocessStage


def test_create_model():
    path = os.path.abspath(os.path.join(__file__, "../../..", 'resources/config.json'))
    config = ConfigStage().run(path)
    model = ModelStage().create_model(config)
    assert isinstance(model, tf.keras.Sequential)


@pytest.mark.parametrize("action", ['train', 'test'])
def test_model_stage(action):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'resources/config.json'))
    config = ConfigStage().run(path)
    images, labels = ExtractStage().run(config, action)

    images, labels = images[:10], labels[:10]
    images, labels = PreprocessStage().run(images, labels, config, action)

    if action == "train":
        model = ModelStage().run(images[:10], labels[:10], config)
    else:
        model = ModelStage().create_model(config)
        model.load_weights(config['model_path'])

    assert isinstance(model, tf.keras.Sequential)
