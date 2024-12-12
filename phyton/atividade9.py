
A = []


for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    A.append(numero)


soma_quadrados = sum([x**2 for x in A])


print(f"\nA soma dos quadrados dos elementos do vetor A é: {soma_quadrados}")
