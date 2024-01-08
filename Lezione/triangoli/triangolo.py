class Triangolo:

    numero_di_triangoli = 0

    def __init__(self, a, b, c):
        Triangolo.numero_di_triangoli += 1 # E' una variabile di classe, non devo usare self perchè non è una variabile di istanza
        self.set_lati(a,b,c)
        self._a = a # Questo valore non è modificabile da altri file direttamente
        self._b = b
        self._c = c
    
    def __str__(self) -> str:
        return f"Il triagolo ha come lati i valori di a = {self._a}, b = {self._b}, c = {self._c}"
    
    def __repr__(self):
        return f"Triangolo({self._a}, {self._b}, {self._c})"

    def __eq__(self, altro): #Equals, come in java
        return (self._a, self._b, self._c) == (altro._a, altro._b, altro._c)

    def set_lati(self, a,b,c):
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError("Attenzione uno dei lati è negativo")

        if not (a + b > c and b + c > a and c + a > b):
            raise ValueError("Attenzione i 3 valori non possono diventare un triangolo")

    def perimetro(self):
        return self._a + self._b + self._c

    @staticmethod
    def posso_formare_triangolo(a, b, c):
        if not (a > 0 and b > 0 and c > 0):
            return False

        if not (a + b > c and b + c > a and c + a > b):
            return False

        return True

    @classmethod
    def crea_equilatero(cls, a):
        return cls(a, a, a) #Scrivere cls(a,a,a) è come far Triangolo(a,a,a)

    @classmethod
    def crea_isoscele(cls, a, b):
        return cls(a, a, b)


    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        if a <= 0:
            raise ValueError("Numero negativo!")
        self._a = a

    @property
    def b(self):
        return self._a

    @b.setter
    def b(self, b):
        if b <= 0:
            raise ValueError("Numero negativo!")
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        if c <= 0:
            raise ValueError("Numero negativo!")
        self._c = c

