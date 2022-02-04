import sys
from orchestration.factory import MessageBrokerFactory


def user(path, broker):

    broker = MessageBrokerFactory().build(broker)
    broker.produce(topic='server', data=path)
    results = broker.consume(topic='user', subscription_name='user')
    print(results)


if __name__ == '__main__':
    user(path=sys.argv[1], broker=sys.argv[2])
