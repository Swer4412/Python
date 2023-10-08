number = 0
count = -1
while number not in (1,2):
    number = int(input('Inserisci il primo intero: '))
    count = count + 1

print(f"riuscito con {count} errori")
    