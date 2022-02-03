import os
import numpy as np
import pytest

from config.stage import ConfigStage
from extract.stage import ExtractStage
from preprocess.stage import PreprocessStage


@pytest.mark.parametrize("action", ['train'])
def test_extract_stage(action):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'resources/config.json'))
    config = ConfigStage().run(path)
    images, labels = ExtractStage().run(config, action)
    images, labels = PreprocessStage().run(images, labels, config, action)
    assert isinstance(images, np.ndarray)
    assert isinstance(labels, np.ndarray)