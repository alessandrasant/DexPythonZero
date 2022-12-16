#Desafio - Calculadora: Faça um programa no qual o usuário vai digitar 2 números e também o tipo de operação que ele gostaria que fosse feita:
#Soma
#Subtração
#Divisão
#Multiplicação
#Potência
#Imprima o resultado para o usuário da operação:
#Num1 Operação Num2

print('_' *130)
print()
print(' ' *50 + 'Calculadora da Lele')
print('_' *130)
print()

numeroUm = float(input('Digite um número a ser calculado: '))
numeroDois = float(input('Digite outro número a ser calculado: '))
operacao = input('Qual operação você deseja realizar? ')

if operacao == 'soma' or operacao == 'Soma':
  calculadora = numeroUm + numeroDois
  print('A soma dos números escolhidos é: {} + {} = {:.2f}'.format(numeroUm, numeroDois, calculadora))
elif operacao == 'subtração' or operacao == 'Subtração':
  calculadora = numeroUm - numeroDois
  print('A subtração dos números escolhidos é: {} - {} =  {:.2f}'.format(numeroUm, numeroDois, calculadora))
elif operacao == 'divisão' or operacao == 'Divisão':
  calculadora = numeroUm / numeroDois
  print('A divisão dos números escolhidos é: {} / {} = {:.2f}'.format(numeroUm, numeroDois, calculadora))
elif operacao == 'multiplicação' or operacao == 'Multiplicação':
  calculadora = numeroUm * numeroDois
  print('A multiplicação dos números escolhidos é: {} * {} = {:.2f}'.format(numeroUm, numeroDois, calculadora))
elif operacao == 'potência' or operacao == 'Potência':
  calculadora = numeroUm ** numeroDois
  print('A potência dos números escolhidos é: {} ** {} = {:.2f}'.format(numeroUm, numeroDois, calculadora))
else:
  print('Você não digitou uma operação válida, tente novamente =)')