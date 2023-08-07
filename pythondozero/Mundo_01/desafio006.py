#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#pede pra o usuário digitar um número e depois armazena esse número na variável 'n' 
#como estamos trabalhando com números inteiros é necessário fazer a conversão para int
n = int(input('Digite um número: '))

#agora calcule o dobro, triplo e a raiz quadrada do número que foi armazenado em 'n'
dobro = n * 2
triplo = n * 3 
raiz = n ** (1/2)

#agora mostre na tela o resultado dos calculos
print(f'Dobro de {n} = {dobro}')
print(f'Triplo de {n} = {triplo}')
print(f'Raiz quadrada de {n} = {raiz}')