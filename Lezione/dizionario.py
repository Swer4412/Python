nazioni = {}

nazioni["it"] = "Italia"
print(nazioni["it"])

nazioni["it"] = "Italy"
print(nazioni)

#Inserimenti
#Ci sono modi diversi
nazioni["pl"] = "polonia"
nazioni.update({"gb" : "gran bretagna"})

#get prende come parametro la chiave e se non esiste mette la stringa che ho scritto
print(nazioni.get("bg", "bg non esite"))

print(nazioni.keys()) #dict_keys(['it', 'gb'])

print(list(nazioni.keys())) #['it', 'gb']

#Chiavi 
for n in nazioni: #Sottointeso nazioni.keys()
    print(n)

#Valori
for n in nazioni.values():
    print(n)

#Chiavi valori
for tupla in nazioni.items(): #Stampa le chiavi e valori una lista
    print(tupla)
    print(tupla[0], tupla[1])

for codice, nazione in nazioni.items():
    print(codice)
    print(nazione)

x, y = 1,2
print(x)
print(y)


diz = {"pl": "polonia", "it" : "Italy", "gb" : "gran bretagna"}

print(diz == nazioni)

#Rimozione
del diz["gb"]

#SET
x = set() # va bene anche x = {}

x.add((1,2))
print(x)
x.add(342)
print(x)
x.add((1,2))
x.add((1,2))
x.add((1,2))
x.add((1,2))
print(x) # output: {(1, 2), 342}

lista = [1,2,3,1,3,45,4,3,4,4,3,4,6,5,4,3,2,3,5,6,6,5,3,4,5,6,4,3,2,3]

#set non garantisce l'ordinamento
set_da_lista = set(lista)

print(set_da_lista)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7}

#Intersezione
s = s1.intersection(s2)
print(s)
print(s1 & s2)

#Unione
s = s1.union(s2)
print(s)
print(s1 | s2)

#Esclusione?
print(s1 - s2) #{1, 2, 3}
print(s2 - s1) #{6, 7}

#Differenza simmetrica
print(s1 ^ s2)

