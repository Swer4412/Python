numeri = list(range(1,6))
a = ""

print(f"numero quadrato cubo")

for n in numeri:
    quad = n**2
    cubo = n**3
    print(f" {n:>5} {quad:>8} {cubo:>4}")