#Exercício 2: Faça um programa que o usuário irá digitar 10 números e você irá mostrar:
#Qual foi o menor valor
#Qual foi o maior valor
#Qual a média dos valores

passo = range(1,10+1)
max = 0
min = 0
soma = 0
qnt = 0

for i in passo:
  n = int(input('Digite um número: '))
  soma += n
  qnt += 1
  if qnt == 1:
    max = min = n
  elif n > max:
    max = n
  elif min > n:
    min = n
  print('numero {}, max {}, min {}, soma {}'.format(n, max, min, soma))

media = soma / i
print('O maior número digitado é: {}, o menor número digitado é: {} e a média dos valores digitados é: {}'.format(max, min, media))

