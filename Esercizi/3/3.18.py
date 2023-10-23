size = int(input("Inserisci quanto devono essere grandi i triangoli: "))

for i in range( size+1):
    print(f"{(i)*'*':<{size}}",f"{(size-i)*'*':<{size}}", f"{(i)*'*':>{size}}", f"{(size-i)*'*':>{size}}")
