from common.stage import UniversalStage
from config.read import ExperimentConfigReader


class ConfigStage(UniversalStage):

    def run(self, config_path):
        config_dict = ExperimentConfigReader().read_json(config_path)

        return config_dict
