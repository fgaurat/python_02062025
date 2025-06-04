from abc import ABC,abstractmethod
# abstract base class

class ICalcGeo(ABC):
    
    @property
    @abstractmethod
    def surface(self):
        pass