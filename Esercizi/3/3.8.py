import math

numeri = []
for i in range(3):
    x = int(input("Inserisci un numero "))
    numeri.append(x)


somma = sum(numeri)
prodotto = 0
for i in range(len(numeri) - 1 ):
    prodotto += numeri[i] * numeri[i+1]

print(prodotto)


'''
min = n1
if n2 < min:
    min = n2
if n3 < min:
    min = n3

max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3

print(somma)
print(prodotto)
print(min)
print(max)
'''