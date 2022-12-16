#Exercício 3
#Dado a mesma tupla do exercício anterior faça um programa que:
#O usuário visualiza o cardápio e digita qual item ele quer comprar. A seguir pergunta se ele quer algo a mais. Caso ele queira vai somando todos os valores do pedido numa variável soma.
#No final printe para o usuário o valor total da conta dele

t1 = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Arroz', 4.5, 'Paçoca', 0.5, 'Pamonha', 5.4)

print('-'*30)
print('-' *10, 'Cardápio', '-' *10)
print('-'*30)
passo = range(0,len(t1))

for i in passo:
  if i%2 == 0:
    print('{:.<20} : R${:5.2f}'.format(t1[i], t1[i+1]))
print('-'*30)

pedido = input('Deseja fazer algum pedido? (s/n) ')
pedido = pedido.lower()
soma = 0

while pedido != 's' and pedido != 'n':
    pedido = input('Essa opção não é válida. Deseja fazer algum pedido? (s/n)')

while pedido =='s':
  pedido2 = input('Digite o seu pedido: ')
  valor = t1.index(pedido2)
  soma += t1[valor+1]
  print('Você pediu: {}, no valor de: R$ {:.2f}'.format(pedido2, t1[valor+1]))
  pedido = input('Deseja mais alguma coisa? (s/n) ')
  while pedido != 's' and pedido != 'n':
    pedido = input('Essa opção não é válida. Deseja fazer mais algum pedido? (s/n)')
print('O valor total do seu pedido foi de: R$ {:.2f}'.format(soma))