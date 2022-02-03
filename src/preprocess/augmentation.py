from tensorflow.keras.preprocessing.image import ImageDataGenerator


def image_augmentation(image, nb_of_augmentation, config):
    """
    Generates new images bei augmentation
    image : raw image
    nb_augmentation: number of augmentations
    images: array with new images
    """

    # Defines the options for augmentation
    datagen = ImageDataGenerator(
        rotation_range=10,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    images = []
    image = image.reshape(1, config["image_dimension"]["img_height"], config["image_dimension"]["img_width"], config["image_dimension"]["channels"])
    i = 0
    for x_batch in datagen.flow(image, batch_size=1):
        images.append(x_batch)
        i += 1
        if i >= nb_of_augmentation:
            # interrupt augmentation
            break
    return images
