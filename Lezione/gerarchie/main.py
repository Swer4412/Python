from abc import ABC, abstractmethod #Abstract Base Class

class Rettangolo(object):
    def __init__(self, base:float, altezza: float) -> None:
        self.base = base
        self.altezza = altezza
        
    def __str__(self) -> str:
        return f"la base è {self.base} e l'altezza è {self.altezza}"
        
        
class Quadrato(Rettangolo):
    def __init__(self, lato) -> None:
        super().__init__(lato, lato)


#classe astrata
class FiguraGeometrica(ABC): #Questa classe implementa una classe astratta di base
    
    @abstractmethod
    def getArea(self):
        raise NotImplementedError("Non implementato")
    
    @abstractmethod
    def getPerimetro(self):
        raise NotImplementedError("Non implementato")


class TriangoloRettangolo(FiguraGeometrica):
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    #Can't instantiate abstract class TriangoloRettangolo with abstract methods getArea, getPerimetro
    def getArea(self):
        return (self.a*self.b) /2
    
    def getPerimetro(self):
        return self.a + self.b + self.c
    
class Studente():
    def __init__(self, nome, altezza) -> None:
        self.nome = nome
        self.altezza = altezza
        
    def __len__(self):
        return self.altezza
    
    def __str__(self):
        return self.nome
        

def main():
    r = Rettangolo(2,5)
    print(r)
    q = Quadrato(2)
    print(q)
    t = TriangoloRettangolo(2,4,3)
    print(t.getArea())
    print(t.getPerimetro())
    
    andrea = Studente("andrea", 190)
    luca = Studente("andrea", 189)
    yousseef = Studente("andrea", 181)
    
    studenti = [andrea, luca, yousseef]
    
    studenti.sort(key=lambda studente: len(studente), reverse=True)
    print(studenti)
    
main()