numeri = list(range(1,6))
a = ""

print(f"numero \t quadrato \t cubo")

for n in numeri:
    quad = n**2
    cubo = n**3
    print(f" {n:>6} {quad:>9} {cubo:>11}")