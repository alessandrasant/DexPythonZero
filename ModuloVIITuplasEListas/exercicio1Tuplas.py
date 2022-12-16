#Exercício: Dada a tupla abaixo:
#t1 = ('Doce', 'Churrasco', 'Bala ', 'Tapioca', 'Pizza ', 'Feijão ', 'Arroz ', 'Açaí ', 'Paçoca ', 'Acarajé', 'Pamonha', 'Dobradinha', 'Rapadura')
#Faça um programa que:
#O usuário digita uma comida e seu programa diz em qual posição do cardápio esse item está
#Printe os itens em ordem alfabética para o usuário

tupla1 = ('Doce', 'Churrasco', 'Bala', 'Tapioca', 'Pizza', 'Feijão', 'Arroz', 'Açaí', 'Paçoca', 'Acarajé', 'Pamonha', 'Dobradinha', 'Rapadura')

print(tupla1)
escolha = input('Digite qual comida você deseja do cardápio: ')
posicao = tupla1.index(escolha)
print(posicao)

sorted(tupla1)
