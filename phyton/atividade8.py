idades = []
alturas = []


for i in range(5):
    idade = int(input(f"Digite a idade da {i+1}º pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    idades.append(idade)
    alturas.append(altura)


print("\nIdades e Alturas na ordem inversa: ")

for i in range(4, -1, -1):
    print(f"Pessoa {i+1}: Idade = {idades[i]}, Altura = {alturas[i]}")