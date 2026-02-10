Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2026
Var
// Seção de Declarações das variáveis
nome:caracter
idade:caracter
gmail:caracter
serie:caracter
primeira_nota:real
segunda_nota:real
soma:real
media:real
resultado:caracter



Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   escreval("informe seu nome: ")
   leia (nome)
   escreval
   
   escreval("informe sua idade: ")
   leia (idade)
   escreval
   
   
   escreval("informe seu gmail: ")
   leia(gmail)
   escreval
   
   escreval(" informe sua serie: ")
   leia(serie)
   escreval
   
   
   
   escreva("primeira nota: ")
   leia(primeira_nota)
   escreval
   

   escreva("segunda nota: ")
   leia(segunda_nota)
   escreval
   

   //processamento

   media <- (primeira_nota + segunda_nota) /2

   se media >=7 entao
   resultado <-"Aprovado"
   senao
   resultado <- ("reprovado")
   fimse


Fimalgoritmo