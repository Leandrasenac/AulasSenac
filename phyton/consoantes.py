listachar = []
consoantes = 0 
print("informe os caracteres: ")
for i in range (10):
    listachar.append((input('Caracter  '+ str(i+1) + ':\n')))
    char = listachar[i]
    if (char not in ("a", "e", "i", "o", "u")):
        consoantes += 1
print(consoantes)