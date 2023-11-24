from getint import get_int

promossi: int = 0
bocciati: int = 0

print("Inserisci 20 valutazioni")
for i in range(20):
    risultato: int = get_int(
        "Inserisci l'esito dell'esame (1=promosso, 2=bocciato): ", 1, 2)
    if risultato == 1:
        promossi += 1
    else:
        bocciati += 1

print(f"Ci sono {promossi} promossi e {bocciati} bocciati")
