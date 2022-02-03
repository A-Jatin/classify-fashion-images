from abc import abstractmethod, ABC


class UniversalStage(ABC):

    @abstractmethod
    def run(self, *args, **kwargs): pass
