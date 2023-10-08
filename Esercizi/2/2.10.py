n1 = int(input("Inserisci un numero "))
n2 = int(input("Inserisci un numero "))
n3 = int(input("Inserisci un numero "))

somma = n1 + n2 + n3
prodotto = n1 * n2 * n3

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