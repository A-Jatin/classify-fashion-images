import os

import numpy as np

from run_image_classifier import run


def test_image_classifier():
    path = os.path.abspath(os.path.join(__file__, "../..", 'resources/config.json'))
    labels = run(path)
    assert isinstance(labels, np.ndarray)
