algoritmo "c�lculo de IMC"
// Fun��o :
// Autor :
// Data : 21/11/2024
// Se��o de Declara��es 
var
   nome: caractere
   imc, peso, altura: real
inicio
// Se��o de Comandos 
   Escreval ("Digite seu nome: ")
   Leia (nome)
   Escreval ("Digite o seu peso: ")
   Leia (peso)
   Escreval ("Digite a sua altura: ")
   Leia(altura)
   imc<- peso / (altura * altura)
   Escreval("O IMC de ", nome, " � ", imc)
fimalgoritmo
