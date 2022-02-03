from model.model import CNN


class ModelBuilderFactory:

    def build(self):
        return CNN()
