# tutte le strutture sono mutabili
import copy

a = [['A', 10], ['B', 20],
     ['C', 30]]
print(a)

# facciamo una shallow copy
b = copy.copy(a)
print(b)

# facciamo la deep copy
b = copy.deepcopy(a)
print(b)

# tutte le strutture sono immutabili

a = (('A', 10), ('B', 20),
     ('C', 30))
print(a)

# facciamo una shallow copy
b = copy.copy(a)
print(b)

# facciamo la deep copy
b = copy.deepcopy(a)
print(b)

# caso misto 1
a = [('A', 10), ('B', 20),
     ('C', 30)]
print(a)

# facciamo una shallow copy
b = copy.copy(a)
print(b)

# facciamo la deep copy
b = copy.deepcopy(a)
print(b)

# caso misto 2
a = (['A', 10], ['B', 20],
     ['C', 30])
print(a)

# facciamo una shallow copy
b = copy.copy(a)
print(b)

# facciamo la deep copy
b = copy.deepcopy(a)
print(b)
