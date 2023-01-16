#Crie uma lista de dicionários contendo as notas de todos os alunos de uma sala (5 alunos). No dicionário é para ter os campos:
#nome:
#nota1:
#nota2:
#media:
#status:
#Peça para o usuário digitar as notas de cada aluno
#Tire a média das notas e adicione no dicionário
#Se média for maior ou igual a 7, coloque "aprovado" no status, caso contrário, coloque "reprovado"
#Calcule a média das médias e imprima para o professor.

alunos = []
boletim = {}
somaMedia = 0
qtdMedia = 0

#Criação das listas dos alunos
for i in range(0,5):
  boletim['nome'] = str(input('Digite o nome do aluno: '))
  boletim['nota1'] = float(input('Digite a primeira nota do aluno: '))
  boletim['nota2'] = float(input('Digite a segunda nota do aluno: '))
  boletim['media'] = (boletim['nota1'] + boletim['nota2'])/2
  if boletim['media'] >= 7:
    boletim['status'] = 'Aprovado'
  else:
    boletim['status'] = 'Reprovado'
  print(boletim)
  alunos.append(boletim.copy())
#Cálculo das médias
for l in alunos:
  for k, v in l.items():
    if k == 'media':
      somaMedia += v
      qtdMedia += 1

mediaDasMedias = somaMedia/qtdMedia

print(alunos)

print(f'A média dos alunos foi de: {mediaDasMedias}.')