#Exercício 2 - Considerando o exercício anterior e considerando que as posições das listas acima são os preços respectivos de:
#Lanche
#Refri
#Batata
#Bombom
#Peça para o usuário informar a quantidade de cada produto que ele irá comprar para depois mostrar o valor total da conta dele.

descricaoProdutos = ('Lanche', 'Refri', 'Batata', 'Bombom')
precoProdutos = (10.9, 5.40, 8.30, 3.40)
qtdComprada = []
somaTotal = 0

print('-'*30)
print('-' *10, 'Cardápio', '-' *10)
print('-'*30)
passo = range(0,len(precoProdutos))

for i in passo:
  print('{:.<20} : R${:5.2f}'.format(descricaoProdutos[i], precoProdutos[i]))
print('-'*30)

for i, valor in enumerate(precoProdutos):
  qtdComprada.append(int(input('Qual a quantidade de {} que você deseja? '.format(descricaoProdutos[i]))))
  somaTotal += (precoProdutos[i]*qtdComprada[i])
print('O preço total da sua compra ficou no valor de {:.2f}'.format(somaTotal))