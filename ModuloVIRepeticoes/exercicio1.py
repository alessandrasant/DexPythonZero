#Exercício 1: Faça um programa que calcula a tabuada do número digitado pelo usuário.

inicio = input('Você deseja saber a tabuada de algum número? (s/n) ')
passo = range (1,10+1)

while inicio == 's':
  num = int(input('Digite um número de 1 a 10: '))
  for i in passo:
    resultado = num * i
    print('{0} * {1:2d} = {2:6d}'.format(num, i, resultado))
  inicio = input('Você deseja saber a tabuada de algum número? (s/n) ')
print('FIM')
