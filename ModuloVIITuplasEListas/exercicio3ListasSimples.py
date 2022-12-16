#Exercício 3 - Faça um programa que pede para o usuário inserir um produto e salvar este produto numa lista.
#Caso o produto já esteja na lista informe uma mensagem de erro e não cadastre o produto duplicado.

listaProdutos = []
descricaoProdutos = input('Insira um produto: ')
listaProdutos.append(descricaoProdutos)
verificacao = 0

adicionarProduto = input('Gostaria de adicionar mais valores a lista? (s/n) ')

while adicionarProduto == 's':
  descricaoProdutos = input('Insira um novo produto: ')
  for i,v in enumerate(listaProdutos):
    if descricaoProdutos == listaProdutos[i]:
      print('O item já está na lista')
      verificacao += 1
  if verificacao == 0:
    listaProdutos.append(descricaoProdutos)
  adicionarProduto = input('Gostaria de adicionar mais valores a lista? (s/n) ')
  verificacao = 0

print(listaProdutos)
