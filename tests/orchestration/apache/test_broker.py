import os

from config.stage import ConfigStage
from orchestration.factory import MessageBrokerFactory


def test_broker():
    path = os.path.abspath(os.path.join(__file__, "../../../..", 'resources/config.json'))
    msgs = []

    config = ConfigStage().run(path)
    broker = MessageBrokerFactory().build(config)

    for msg in broker.run(data=['hello', 'world']):
        msgs.append(msg)
    assert len(msgs) == 2
