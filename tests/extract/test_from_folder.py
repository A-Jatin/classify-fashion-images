import os

import numpy as np

from config.stage import ConfigStage
from extract.extract_data import extract_data_from_folder


def test_extract_from_folder():
    path = os.path.abspath(os.path.join(__file__, "../../..", 'resources/config.json'))
    config = ConfigStage().run(path)
    images, _ = extract_data_from_folder(config)
    assert isinstance(images, np.ndarray)