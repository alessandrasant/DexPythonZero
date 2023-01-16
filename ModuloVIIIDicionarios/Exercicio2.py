#Adapte o sistema anterior para que as notas 1 e 2 estejam dentro de uma lista. Então o dicionário irá conter:
#nome:
#nota: [nota1 nota2]
#media:
#status:
#Peça para o usuário digitar as notas de cada aluno
#Tire a média das notas e adicione no dicionário
#Se média for maior ou igual a 7, coloque "aprovado" no status, caso contrário, coloque "reprovado"
#Calcule a média das médias e imprima para o professor.

alunos = []
boletim = {}
notas = []
somaMedia = 0
qtdMedia = 0

for i in range(0,5):
  boletim['nome'] = str(input('Digite o nome do aluno: '))
  notas.append(float(input('Digite a primeira nota do aluno: ')))
  notas.append(float(input('Digite a segunda nota do aluno: ')))
  boletim['nota'] = notas.copy()
  boletim['media'] = (boletim['nota'][0] + boletim['nota'][1])/2
  if boletim['media'] >= 7:
    boletim['status'] = 'Aprovado'
  else:
    boletim['status'] = 'Reprovado'
  print(boletim)
  notas.clear()
  alunos.append(boletim.copy())

for l in alunos:
  for k, v in l.items():
    if k == 'media':
      somaMedia += v
      qtdMedia += 1

mediaDasMedias = somaMedia/qtdMedia

print(alunos)

print(f'A média dos alunos foi de: {mediaDasMedias}.')