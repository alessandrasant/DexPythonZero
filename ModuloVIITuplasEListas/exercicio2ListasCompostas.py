#Exercício 2 - Faça um programa que irá mostrar item a item do cardápio para o usuário e irá perguntar quantos daquele item a pessoa quer comprar.
#No final mostre a quantidade de cada item comprado e também o valor total da compra.

cardapio = [['Lanche', 10.9], ['Batata',  5.5], ['Refri' ,  3.9]]
soma = 0
listaQtd = []

for c in cardapio:
  print('-' *30)
  print(f'{c[0]:.<19}....R${c[1]:5.2f}')
  print('-' *30)
  valor = int(input('Quantas unidades desse item você vai querer? '))
  listaQtd.append(valor)
  soma += valor*c[1]
print('-'*30)

print(f'Você pediu {listaQtd[0]} Lanches, {listaQtd[1]} Batatas e {listaQtd[2]} Refris. A sua conta total ficou no valor de: R$ {soma:.2f}')
