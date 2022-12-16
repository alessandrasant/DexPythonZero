#Exercício 3: Faça um programa no qual o usuário insira 2 inteiros. Verifique se o número 1 é divisível pelo número 2. Imprima essa informação para o usuário.

numeroUm = int(input('Digite um número inteiro: '))
numeroDois = int(input('Digite outro número inteiro: '))

verificacao = numeroUm % numeroDois

if verificacao == 0:
  print('O primeiro número que você digitou foi: {} e ele é divisível pelo segundo número que você digitou: {}'.format(numeroUm,numeroDois))
else:
  print('O primeiro número que você digitou foi: {} e ele não é divisível pelo segundo número que você digitou: {}'.format(numeroUm,numeroDois))