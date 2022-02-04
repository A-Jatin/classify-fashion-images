import os
from google.cloud import pubsub_v1

from orchestration.common.broker import MessageBroker


class GcpMessageBroker(MessageBroker):

    def produce(self, topic, data=None, *args, **kwargs):
        """

        :param topic: topic name that you created: format 'projects/{project_id}/topics/{topic}'
        :param data:
        :param args:
        :param kwargs:
        :return:
        """
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
            topic=topic
        )
        publisher = pubsub_v1.PublisherClient()
        future = publisher.publish(topic_name, data, spam='eggs')
        future.result()

    def consume(self, topic, subscription_name, *args, **kwargs):
        """

        :param topic:
        :param subscription_name: format 'projects/{project_id}/subscriptions/{my_subscription_name}'
        :param args:
        :param kwargs:
        :return:
        """
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
            topic=topic
        )

        subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
            project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
            sub=subscription_name
        )

        def callback(message):
            print(message.data)
            message.ack()
        with pubsub_v1.SubscriberClient() as subscriber:
            subscriber.create_subscription(
                name=subscription_name, topic=topic_name)
            future = subscriber.subscribe(subscription_name, callback)

        return future.result()


