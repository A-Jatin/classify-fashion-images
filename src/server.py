import os
import sys

from orchestration.factory import MessageBrokerFactory
from run_image_classifier import run


def server():
    #os.system(kafka_path+"/bin/kafka-topics.sh --create --topic user --bootstrap-server localhost:9092")
    #os.system(kafka_path+"/bin/kafka-topics.sh --create --topic server --bootstrap-server localhost:9092")
    broker = MessageBrokerFactory().build('apache', subscription_name = 'server;)
    path = broker.consume(topic='user')
    labels = run(path)
    broker.produce(topic='server', data=labels)


if __name__ == '__main__':
    server()
