import os

from config.stage import ConfigStage


def test_config_stage():
    path = os.path.abspath(os.path.join(__file__, "../../..", 'resources/config.json'))
    config = ConfigStage().run(path)
    assert "actions" in config.keys()
    assert "path" in config.keys()
    assert "model_path" in config.keys()
