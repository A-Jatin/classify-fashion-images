import os
from confluent_kafka import Producer
from confluent_kafka import Consumer

from orchestration.common.broker import MessageBroker


class ApacheMessageBroker(MessageBroker):

    def delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    def produce(self, topic, data=None, *args, **kwargs):

        p = Producer({'bootstrap.servers':  'localhost:9092'})

        for message in data:
            # Trigger any available delivery report callbacks from previous produce() calls
            p.poll(0)

            # Asynchronously produce a message, the delivery report callback
            # will be triggered from poll() above, or flush() below, when the message has
            # been successfully delivered or failed permanently.
            p.produce(topic, message.encode('utf-8'), callback=self.delivery_report)

        # Wait for any outstanding messages to be delivered and delivery report
        # callbacks to be triggered.
        p.flush(30)

    def consume(self, topic, *args, **kwargs):
        c = Consumer({
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'mygroup',
            'session.timeout.ms': 6000
        })

        c.subscribe([topic])
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue
            print('Received message: {}'.format(msg.value().decode('utf-8')))
            return msg.value().decode('utf-8')
        c.close()

    def terminate(self, *args, **kwargs):
        os.system("rm -rf /tmp/kafka-logs /tmp/zookeeper")
