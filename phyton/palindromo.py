

def criar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(".", "")
    invertido = texto [::-1]

    if texto == invertido:
        return True
    else:
        return False
    
entrada = input("Digite uma palavra ou frase: ")
if criar_palindromo(entrada):
    print("A entrada é um palíndromo! ")
else:
    print("A entrada não é um palíndromo...")