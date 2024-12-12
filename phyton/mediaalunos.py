listanotas= []
notasaluno= []
print("Informe a nota dos alunos: ")
for i in range(10):
    media = 0 
    notasaluno =[]
    print("Aluno " + str(i+1))
for j in range(4):
    notasaluno.append(float(input("Nota " + str(j+1) + "\n")))
    media += notasaluno[j]
    print(media)
    media/4
    listanotas.append(media)
print(listanotas)