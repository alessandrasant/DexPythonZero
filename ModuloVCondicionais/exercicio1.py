#Exercício 1: Faça um programa que verifique se o usuário digitou um valor numérico ou não.
# Caso Verdadeiro, imprima: 'Esse input é um número'
# Caso Falso, imprima: 'Esse input não é um número, tente novamente'

valor = input('Digite algo: ')

intTeste = valor.isnumeric()

if intTeste == True:
  print('Esse input é um número.')
else:
  print('Esse input não é um número, tente novamente.')