item = 0
lista = []

while item != "":
    item = input("Inserisci qualcosa: ")
    lista.append(item)

lista.pop()
lista = sorted(list(set(lista)), reverse=True)
print(lista)