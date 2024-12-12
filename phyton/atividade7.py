numeros = []

for i in range(5):
    numero= int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma= sum(numeros)
multiplicacao = 1

for numero in numeros:
    multiplicacao *=numero


print(f"\nNúmeros Digitados: {numeros}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")