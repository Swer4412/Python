from abc import ABC, abstractmethod 

class FiguraGeometrica(ABC):
    
    @abstractmethod
    def getArea(self) -> float:
        raise NotImplementedError
    
    @abstractmethod
    def getPerimetro(self) -> float:
        raise NotImplementedError
    
    @abstractmethod
    def getTriangolo(self):
        raise NotImplementedError
    
    