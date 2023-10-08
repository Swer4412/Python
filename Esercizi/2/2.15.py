n1 = input("inserisci un numero non intero ")
n2 = input("inserisci un numero non intero ")
n3 = input("inserisci un numero non intero ")

numeri = [n1, n2, n3]

if numeri[0] > numeri[1]:
    copia = numeri[0]
    numeri[0] = numeri[1]
    numeri[1] = copia

if numeri[1] > numeri[2]:
    copia = numeri[1]
    numeri[1] = numeri[2]
    numeri[2] = copia

if numeri[0] > numeri[2]:
    copia = numeri[0]
    numeri[0] = numeri[2]
    numeri[2] = copia

#non so farlo :(
print(numeri.sort())