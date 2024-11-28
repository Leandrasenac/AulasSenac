valorEmp = juros = parcelas = rJuros = resposta = float

valorEmp = float(input("Quanto vou pagar de empréstimo?: R$ "))
juros = float(input("Qual o valor dos juros cobrados pelo banco em %? "))
parcelas = float (input("Quantas parcelas quero dividir para pagar? "))
rJuros = ((valorEmp * juros) /100)

print("O valor do meu juros será de R$", rJuros)
resposta = (rJuros + valorEmp) / parcelas




print("O valor das", parcelas,"parcelas que terei que pagar é de R$ ", resposta)