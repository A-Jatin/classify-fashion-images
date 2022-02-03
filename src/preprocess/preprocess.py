import tensorflow as tf
import numpy as np

from preprocess.augmentation import image_augmentation


def preprocess_data(images, targets, config, use_augmentation=False, nb_of_augmentation=1):
    """
    images: raw image
    targets: target label
    use_augmentation: True if augmentation should be used
    nb_of_augmentation: If use_augmentation=True, number of augmentations
    """
    X = []
    y = []
    for x_, y_ in zip(images, targets):

        # scaling pixels between 0.0-1.0
        x_ = x_ / 255.

        # data Augmentation
        if use_augmentation == 1:
            argu_img = image_augmentation(x_, nb_of_augmentation, config)
            for a in argu_img:
                X.append(a.reshape(config["image_dimension"]["img_height"], config["image_dimension"]["img_width"], config["image_dimension"]["channels"]))
                y.append(y_)

        X.append(x_.reshape(config["image_dimension"]["img_height"], config["image_dimension"]["img_width"], config["image_dimension"]["channels"]))
        y.append(y_)
    print('*Preprocessing completed: %i samples\n' % len(X))
    return np.array(X), tf.keras.utils.to_categorical(y)
