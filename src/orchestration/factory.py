from orchestration.apache.broker import ApacheMessageBroker


class MessageBrokerFactory:

    def build(self, broker):

        if broker == 'apache':
            return ApacheMessageBroker()
