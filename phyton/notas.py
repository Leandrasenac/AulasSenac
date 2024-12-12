listanotas=[]
media=0
print("Informe as 4 notas: ")
for i in range(4):
    listanotas.append(float(input("Nota"+ str(i+1)+ ":\n")))
    media += listanotas[i]
media/4
print(listanotas)
print(media)