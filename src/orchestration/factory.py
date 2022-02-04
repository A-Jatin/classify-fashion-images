from orchestration.apache.broker import ApacheMessageBroker
from orchestration.gcp.broker import GcpMessageBroker


class MessageBrokerFactory:

    def build(self, broker):

        if broker == 'apache':
            return ApacheMessageBroker()
        
        if broker == 'gcp':
            return GcpMessageBroker()
