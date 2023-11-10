testo = "ciao questo è un testo di prova per vedere quante volte viene scritto una certa parola tipo testo oppure parole oppure volte"

lista_parole = testo.split()

frequenze={}

for parola in lista_parole:
    if parola not in frequenze:
        frequenze[parola] = 1
    else :
        frequenze[parola] += 1
        
# Pazzurdo, 
frequenze_ordinato = sorted(frequenze.items(), key=lambda tupla:tupla[1], reverse=True) #Key vuol dire che funzione deve

print(frequenze_ordinato)