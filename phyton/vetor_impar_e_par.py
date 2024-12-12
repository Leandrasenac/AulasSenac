listapar = []
listaimpar = []
listanumeros = []
numero=0

print("Informe os números: ")
for i in range(20):
    listanumeros.append(int(input("Número " + str(i+1)+ ":\n")))
    numero = listanumeros[i]
    print(numero)
    if(numero%2 == 0):
        listapar.append(numero)
    else:
        listaimpar.append(numero)

print(listanumeros)
print(listapar)
print(listaimpar)