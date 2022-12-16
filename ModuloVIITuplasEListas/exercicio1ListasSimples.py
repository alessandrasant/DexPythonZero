#Exercício 1: Dada as listas e tuplas abaixo:
#preco = (10.9, 5.40, 8.30, 3.40)
#qtdComprada = [0, 3, 2, 4]
#Calcule e mostre para o usuário o valor total da compra dele sendo que o valor total será a soma da multiplicação do preço do produto pela quantidade comprada.

preco = (10.9, 5.40, 8.30, 3.40)
qtdComprada = [0, 3, 2, 4]
somaTotal = 0

for i, valor in enumerate(preco):
  somaTotal += (preco[i]*qtdComprada[i])
print('O preço total da sua compra ficou no valor de {:.2f}'.format(somaTotal))