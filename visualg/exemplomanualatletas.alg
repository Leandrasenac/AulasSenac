algoritmo "Classifica��o de Atletas"
// Fun��o :
// Autor :
// Data : 25/11/2024
// Se��o de Declara��es 
var
   nome, categoria: caractere
   idade: inteiro
inicio
// Se��o de Comandos 
   Escreval("Nome do Atleta: ")
   Leia(Nome)
   Escreval("Idade do Atleta: ")
   Leia(idade)
   Escolha idade
   caso 5, 6, 7, 8, 9, 10
        categoria <- "Infantil"
   caso 11, 12, 13, 14, 15
        categoria <- "Juvenil"
   caso 16, 17, 18, 19, 20
        categoria <- "Junior"
   caso 21, 22, 23, 24, 25
        categoria <- "Profissional"
   outrocaso
            categoria <- "INVALIDO"
   Fimescolha
   Escreval("categoria = ", categoria)
fimalgoritmo
