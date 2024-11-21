algoritmo "cálculo de IMC"
// Função :
// Autor :
// Data : 21/11/2024
// Seção de Declarações 
var
   nome: caractere
   imc, peso, altura: real
inicio
// Seção de Comandos 
   Escreval ("Digite seu nome: ")
   Leia (nome)
   Escreval ("Digite o seu peso: ")
   Leia (peso)
   Escreval ("Digite a sua altura: ")
   Leia(altura)
   imc<- peso / (altura * altura)
   Escreval("O IMC de ", nome, " é ", imc)
fimalgoritmo
