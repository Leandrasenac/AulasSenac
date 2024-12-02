numero = int(input("Verificar números primos até: "))
mult = 0

for count in range (2,numero):
    if (numero % count == 0):
        print("Multiplo de: ", count)
        mult + 1
if mult == 0:
    print("Esse número é primo")
else:
    print("Tem",mult,"multiplos acima de 2 e abaixo de", numero)
