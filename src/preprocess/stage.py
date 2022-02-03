from common.stage import UniversalStage
from preprocess.preprocess import preprocess_data


class PreprocessStage(UniversalStage):

    def run(self, images, labels, config, action):

        images, labels = preprocess_data(images, labels, config, use_augmentation=bool(config['use_augmentation'][action]), nb_of_augmentation=1)

        return images, labels
