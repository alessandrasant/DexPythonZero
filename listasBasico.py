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
