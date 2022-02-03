from config.stage import ConfigStage
from extract.extract_data import extract_data_from_folder
from orchestration.factory import MessageBrokerFactory
from preprocess.stage import PreprocessStage


def run(path):
    config = ConfigStage().run(path)
    images, labels = extract_data_from_folder(config)
    images, labels = PreprocessStage().run(images, labels, config, action='test')
    broker = MessageBrokerFactory().build(config)

    for msg in broker.run(data=images):
        images.append(msg)
