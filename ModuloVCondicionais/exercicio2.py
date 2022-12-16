#Exercício 2: Peça para o usuário digitar um número e verifique se ele é par e imprima para o usuário essa informação.

numero = input('Digite um número para saber se ele é par: ')

verificacao = numero.isnumeric()

if verificacao == True:
  par = int(numero)%2
  if par == 0:
    print('O número que você digitou foi: {} e ele é par.'.format(numero))
  else:
    print('O número que você digitou foi: {} e ele não é par.'.format(numero))
else:
  print('Você não digitou um número, tente novamente.')

