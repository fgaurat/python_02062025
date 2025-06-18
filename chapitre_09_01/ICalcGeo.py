from abc import ABC,abstractmethod,ABCMeta
# abstract base class

# class ICalcGeo(metaclass=ABCMeta):
class ICalcGeo(ABC):
    
    @property
    @abstractmethod
    def surface(self):
        pass