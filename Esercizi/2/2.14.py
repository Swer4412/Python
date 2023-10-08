max_beat= 220

age = int(input("Inserisci l'età: "))

max_beat = max_beat - age

print("Battito massimo: ", max_beat)
print("Intervallo frequenza: ", int(max_beat * 0.5), " ", int(max_beat * 0.85))