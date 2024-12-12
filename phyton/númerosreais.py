lista_numeros_reais = []
print("Informe os 10 números reais")
for i in range(10):
    lista_numeros_reais.append(float(input("Número"+ str(i + 1)+ ":\n")))
lista_numeros_reais.reverse()
print(lista_numeros_reais)