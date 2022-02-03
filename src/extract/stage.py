from common.stage import UniversalStage
from extract.extract_data import extract_data_from_gz


class ExtractStage(UniversalStage):

    def run(self, config, action):

        images, label = extract_data_from_gz(config, action)

        return images, label
