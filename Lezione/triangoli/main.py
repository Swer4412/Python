from triangolo import Triangolo

def main():
    t = Triangolo(2, 2, 3)
    f = Triangolo(2, 2, 3)
    print(t.perimetro())

    #Per chiamare il metodo statico, si richiama il metodo direttamente dalla classe
    print(Triangolo.posso_formare_triangolo(3,2,3))

    print(Triangolo.crea_equilatero(2).perimetro()) # 6

    print(Triangolo.numero_di_triangoli)

    print(t == f) #Per richiamare un equals bisogna scrivere ==

if __name__ == "__main__":
    main()
