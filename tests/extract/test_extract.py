import numpy as np
import pytest
import os

from config.stage import ConfigStage
from extract.stage import ExtractStage


@pytest.mark.parametrize("action", ['test'])
def test_extract_stage(action):
    path = os.path.abspath(os.path.join(__file__, "../../..", 'resources/config.json'))
    config = ConfigStage().run(path)
    images, labels = ExtractStage().run(config, action)
    assert isinstance(images, np.ndarray)
    assert isinstance(labels, np.ndarray)
