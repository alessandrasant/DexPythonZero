#Exercício 2: Faça um programa que o usuário digita um valor inteiro e nós mostramos toda a tabuada daquele número.

var = int(input('Digite um número inteiro: '))
print('-' *20)

zero = var*0
um = var*1
dois = var*2
tres = var*3
quatro = var*4
cinco = var*5
seis = var*6
sete = var*7
oito = var*8
nove = var*9
dez = var*10

print('{0} * 0 = {1:6d}'.format(var, zero))
print('{0} * 0 = {1:6d}'.format(var, um))
print('{0} * 0 = {1:6d}'.format(var, dois))
print('{0} * 0 = {1:6d}'.format(var, tres))
print('{0} * 0 = {1:6d}'.format(var, quatro))
print('{0} * 0 = {1:6d}'.format(var, cinco))
print('{0} * 0 = {1:6d}'.format(var, seis))
print('{0} * 0 = {1:6d}'.format(var, sete))
print('{0} * 0 = {1:6d}'.format(var, oito))
print('{0} * 0 = {1:6d}'.format(var, nove))
print('{0} * 0 = {1:6d}'.format(var, dez))