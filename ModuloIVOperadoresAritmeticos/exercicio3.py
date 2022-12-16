#Exercício 3: Faça um programa no qual o usuário digite a distância percorrida por um carro e a qtd de litros de combustível gasto. Calcule e mostre para o usuário quantos km/l o seu carro faz.

kmRodados = float(input('Quantos km você rodou com seu carro? '))
litrosGastos = float(input('Quantos litros de combustível foi gasto? '))
resultado = kmRodados/litrosGastos

print('O seu carro faz: {:.2f} km/l'.format(resultado))