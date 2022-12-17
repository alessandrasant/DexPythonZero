#Exercício 1 - Dada a lista:
#cardapio = [['Lanche', 10.9], ['Batata',  5.5], ['Refri' ,  3.9]]
#Faça um programa que irá mostrar o cardápio do restaurante de forma organizada.

cardapio = [['Lanche', 10.9], ['Batata',  5.5], ['Refri' ,  3.9]]

print('-' *30)
print('-'*10 + ' Cardápio ' + '-' *10)
print('-' *30)

for c in cardapio:
  print(f'{c[0]:.<19}....R${c[1]:5.2f}')
print('-'*30)