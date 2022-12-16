#Exercício 2: Dado a tupla abaixo:
#t1 = ('Doce', 2.3, 'Bala ', 0.15, 'Pizza ', 28.9, 'Arroz ', 4.5, 'Paçoca ', 0.5, 'Pamonha', 5.4)
#Os dados estão organizados de forma que tem o valor do produto e logo após o seu preço. Faça um programa que mostre o cardápio de forma organizada.

t1 = ('Doce', 2.3, 'Bala ', 0.15, 'Pizza ', 28.9, 'Arroz ', 4.5, 'Paçoca ', 0.5, 'Pamonha', 5.4)

print('-'*30)
print('-' *10, 'Cardápio', '-' *10)
print('-'*30)
passo = range(0,12)

for i in passo:
  if i%2 == 0:
    print('{:.<20} : R${:5.2f}'.format(t1[i], t1[i+1]))
print('-'*30)
