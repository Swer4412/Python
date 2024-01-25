from figura_geometrica import FiguraGeometrica
from math import sqrt
from tipo_triangolo import TipoTriangolo

class Triangolo(FiguraGeometrica):
    
    def __init__(self, a, b, c):
        if not (a + b > c or a + c > b or b + c > a):
            raise ValueError("Un lato è più lungo della somma degli altri")

        if not (a > 0 or b > 0 or c > 0):
            raise ValueError("Impossibile creare un triangolo con lato minore di 0")

        self.__a = a
        self.__b = b
        self.__c = c
        self.__p = (a + b + c)/2


    def getArea(self):
        return sqrt(self.__p*(self.__p-self.__a)*(self.__p-self.__b)*(self.__p-self.__c))
    
    def getPerimetro(self):
        return self.__p * 2
    
    def getTriangolo(self):
        if (self.__a == self.__b == self.__c):
            return TipoTriangolo.EQUILATERO
        if (self.__a == self.__b or self.__a == self.__c or self.__b == self.__c):
            return TipoTriangolo.ISOSCELE

        return TipoTriangolo.SCALENO

    def __str__(self):
        return "Triangolo" + self.__a + self.__b + self.__c

    def __len__(self):
        return self.getArea()
    
    