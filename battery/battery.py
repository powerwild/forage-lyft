from abc import ABC, abstractmethod

class Battery(ABC):

    @abstractmethod
    def needs_service(self):
        pass

    @abstractmethod
    def perform_service(self):
        pass
