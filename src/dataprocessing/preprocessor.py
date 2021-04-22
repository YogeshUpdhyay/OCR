from abc import ABC

class Preprocessor(ABC):
    @abc.abstractmethod
    def get_cells(self):
        pass
    