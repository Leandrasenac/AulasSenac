nome = str
imc = peso = altura = float

nome=str(input("Digite seu nome: "))

peso=float(input("Digite seu peso: "))

altura=float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("O IMC de ", nome,"é", imc)