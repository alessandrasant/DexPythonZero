#Exercicio 3
#Dada os dois dicionários abaixo, calcule a média de preços:
#produtos = [ {
#          'produto': 'maça',
#          'preco': 2.2
#          },
#         {
#          'produto': 'banana',
#          'preco': 1.2
#          } ]
#everton = {
#        'cliente': 'Everton'
#        'compra': [ {
#                      'produto': 'maça',
#                      'qtd' = 3
#                     },
#                    {
#                      'produto': 'banana',
#                      'qtd' = 10
#                     } ]
#}

#Calcule o valor total da compra do Everton
#Imprima a qtd que ele comprou e o que ele comprou
#Imprima o valor total das compras

produtos = [ {
          'produto': 'maça',
          'preco': 2.2
          },
         {
          'produto': 'banana',
          'preco': 1.2
          } ]
everton = {
        'cliente': 'Everton',
        'compra': [ {
                      'produto': 'maça',
                      'qtd': 3
                     },
                    {
                      'produto': 'banana',
                      'qtd': 10
                     } ]
}

soma = 0

for v in everton['compra']:
  qtd = v['qtd']
  for p in produtos:
    if p['produto'] == v['produto']:
      soma += qtd * p['preco']
      print(f"Everton comprou {v['qtd']} {p['produto']}s, custando R${p['preco']} cada.")

print(f'A compra no total ficou no valor de: R${soma}')