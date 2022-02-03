from abc import ABC, abstractmethod


class MessageBroker(ABC):

    @abstractmethod
    def produce(self, *args, **kwargs): pass
    
    @abstractmethod
    def consume(self, *args, **kwargs): pass
