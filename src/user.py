import sys
from orchestration.factory import MessageBrokerFactory


def user(path):

    broker = MessageBrokerFactory().build('apache')
    broker.produce(topic='server', data=path)
    results = broker.consume(topic='user')
    print(results)


if __name__ == '__main__':
    user(path=sys.argv[1])
