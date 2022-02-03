import gzip
import logging
import numpy as np
import os
from PIL import Image

log = logging.getLogger(__name__)


def common_resources():
    return os.path.abspath(os.path.join(__file__, "../../..", "resources/data"))


def extract_data_from_gz(config, action):
    """
    Extract images of an idx byte file
    ----------
    config:
    action:
    """

    data_folder = common_resources()
    images_path = data_folder + "/" + config["path"][action]["images"]
    labels_path = data_folder + "/" + config["path"][action]["labels"]

    labels_path = os.path.join(labels_path)
    images_path = os.path.join(images_path)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8,
                               offset=8)

    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8,
                               offset=16).reshape(len(labels), 784)

    return images, labels


def extract_data_from_folder(config):
    images = []
    data_folder = common_resources() + "/" +config["predict_path"]
    image_paths = os.listdir(data_folder)
    for image_path in image_paths:
        image = Image.open(data_folder+'/'+image_path)
        images.append(np.asarray(image))

    images = np.array(images)
    return images, np.zeros(images.shape[0])

