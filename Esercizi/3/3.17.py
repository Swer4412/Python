size = int(input("Inserisci quanto devono essere grandi i triangoli: "))

for i in range(size+1):
    print("*"*i)

print()

for i in range(size, 0, -1):
    print('*'*i)

print()

for i in range(size, 0, -1):
    print(f"{'*'*i:>{size}}")

print()

for i in range(size+1):
    print(f"{'*'*i:>{size}}")