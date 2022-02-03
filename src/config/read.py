import json
import unicodedata


class ExperimentConfigReader:

    def remove_control_characters(self, s):
        return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

    def read_json(self, path_):
        with open(path_, 'r') as file:
            data = file.read().replace('\n', '')
            data = self.remove_control_characters(data)
            data = json.loads(data)
            return data
