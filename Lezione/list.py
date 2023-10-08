import random
import time
import statistics as stats

a = []
for x in range(10):
    a.append(2*x)

print(a)

#List comprehension
a = [2*x for x in range(10)]
print(a)

start = time.time
voti = [random.randint(1,100) for _ in range(1_000)]
end = time.time
print(voti)

#statistics
print(sum(voti))
print(stats.mean(voti)) #media
print(stats.median(voti)) #mediana
print(stats.mode(voti)) #moda

'''
somma = 0
cont = 0
finito = False
while not finito:
    voto = int(input("Dammi un voto "))

    if voto == -1:
        finito = True
    else: 
        cont += 1
        somma += voto
'''
x=87
for index, voto in enumerate(voti):
    if voto == x:
        print(voto)
        break #serve perchè se no else non viene visto
else:
    print(f"{x} Non trovato!")
