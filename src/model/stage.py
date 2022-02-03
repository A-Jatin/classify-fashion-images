import os
from sklearn.model_selection import train_test_split

from common.stage import UniversalStage
from model.factories import ModelBuilderFactory


def common_resources():
    return os.path.abspath(os.path.join(__file__, "../../..", "resources"))


class ModelStage(UniversalStage):

    def create_model(self, config):
        model = ModelBuilderFactory().build()
        model = model.create_model(config)
        return model

    def run(self, X, y, config):

        X_train_, X_val_, y_train_, y_val_ = train_test_split(X, y,
                                                              test_size=0.2, random_state=42)

        model = self.create_model(config)

        model.fit(
            X_train_, y_train_,
            batch_size=config["batch_size"],
            epochs=config["num_epochs"],
            verbose=1,
            validation_data=(X_val_, y_val_)
        )

        model_path = common_resources() + '/' + config["model_path"]
        model.save_weights(model_path, overwrite=True)

        return model


