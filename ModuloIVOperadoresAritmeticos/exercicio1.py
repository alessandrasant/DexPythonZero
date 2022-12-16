#Exercício 1: Criar variáveis n1 e n2 que receberão inputs do tipo INT do usuário. Exibir o resultado da Adição dessas 2 variáveis. Exibir o resultado da Subtração dessas variáveis. Exibir o resultado da Multiplicação dessas variáveis. Exibir o resultado da Divisão dessas variáveis. Exibir o resultado do Módulo (Resto da divisão) entre essas variáveis. Exibir o resultado de uma variável Exponenciando a outra.

n1 = int(input('Escolha um número para ser calculado: '))
n2 = int(input('Escolha o segundo número a ser calculado: '))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1*n2
divisao = n1 / n2
modulo = n1%n2
exponencial = n1 ** n2

print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao)
print(modulo)
print(exponencial)