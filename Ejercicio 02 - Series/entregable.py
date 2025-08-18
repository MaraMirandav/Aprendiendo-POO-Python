from abc import ABC, abstractmethod

class Entregable(ABC):

    @abstractmethod
    def entregar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass

    @abstractmethod
    def is_entregado(self):
        pass

    @abstractmethod
    def compare_to(self):
        pass