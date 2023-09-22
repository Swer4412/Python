investimento = 1000
rendimento = 0.07

for i in range(31):
    if i % 10 == 0:
        print(investimento*(1 + rendimento)**i)