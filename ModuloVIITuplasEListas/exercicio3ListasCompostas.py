#Exercício 3 - Faça um programa que o usuário cadastre algumas informações sobre clientes:
#nome
#email
#telefone
#idade
#A seguir faça um sistema de pesquisa no qual o usuário digita o email e o sistema mostra todas as informações deste usuário.

base_de_dados = []
cliente = []

input_cliente = input('Deseja cadastrar dados na base de dados? (s/n)')

while input_cliente == 's':
  cliente.append(str(input('Digite o nome do cliente: ')))
  cliente.append(str(input('Digite o e-mail do cliente: ')))
  cliente.append(str(input('Digite o telefone do cliente: ')))
  cliente.append(int(input('Digite a idade do cliente: ')))
  base_de_dados.append(cliente[:])
  print(f'Cliente = {cliente} e Base de dados = {base_de_dados}')
  cliente.clear()
  input_cliente = input('Deseja cadastrar dados na base de dados? (s/n)')

print('-=' *30)
print(f'{"No.":<5}{"E-MAIL"}')
print('-'*30)

for i, nome in enumerate(base_de_dados):
  print(f'{i:<5}{nome[1]}')
print('-'*30)

while True:
  opc = int(input('Mostrar dados de qual cliente: (Digite 999 para finalizar) ' ))
  if opc == 999:
    break
  if opc <= len(base_de_dados) - 1:
    print(f'Dados de {base_de_dados[opc][0]}: \n E-mail: {base_de_dados[opc][1]} \n Telefone: {base_de_dados[opc][2]} \n Idade: {base_de_dados[opc][3]}')

