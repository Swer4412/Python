x : int = 3
print(id(x), x)
x = x + 1
print(id(x), x)
x = "ciao"
print(id(x), x)

lista = ["cane", "gatto", "pollo", "cavallo", 10, True, ("can", "gat")]

for i in range(len(lista)): #Non pythonico
    print(i)

for i in lista: #Pythonico
    print(i)

print(list(enumerate(lista)))
for index, el in enumerate(lista): #Con indici
    print(index, el)

print(2323456789876543456789*3456789876543456789*3456789098765456789*4567890*987654567876543212345678987654323456*987654345678909876543212345678987654323456789098765432*98765434567898765434567*97896986955674688678543678796543243657*9685746345243657868675432467*89678543565789786857534*456788765465879785436475843567456432543678673444356564436776543675756743364*64569857463565768574367867079685743123245768787564323435676878564353254364758679764532543647587856432543687867456*78645326478908976543536758698765434536478979563443647766756447657*985432436478697564236789)
lista[6] = "dio"
print(lista)

tupla = (1,2,3)
nuova_tupla = tupla + (4,) #Metti (4,) per dirgli che è una tupla
print(nuova_tupla)
print(tupla)

x = int(input("Dammi un numero qualsiasi "))
y = int(input("Dammi un numero qualsiasi "))
z = int(input("Dammi un numero qualsiasi "))

min = x

if y < min:
    min = y

if z < min:
    min = z

print(min)
