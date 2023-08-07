#faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

#pede um número inteiro ao usuário e armazena o número em 'n'
#como estamos trabalhando com números inteiros é necessário fazer a conversão para int
n = int(input('Digite um número inteiro para ver a sua tabuada de multiplicação do 1 ao 10.\n: '))

#isso abaixo é só um pequena decoração. estou pedindo para o computador mostra o nome tabuada centralizado e com sinais de '=' a sua esquerda e a sua direita 
#o nome tabuada vai ficar assim ---> '==tabuada==' 
t = 'Tabuada'
print('{:=^30}'.format(t))

#agora faça os calculos e mostre na tela a tabuada de 1 a 10 do número que foi digitado
#para agilizar, eu fiz o calculo da multiplicação dentro do .format mesmo
print('{0} x {1} = {2}'.format(n, 1, (n*1)))
print('{0} x {1} = {2}'.format(n, 2, (n*2)))
print('{0} x {1} = {2}'.format(n, 3, (n*3)))
print('{0} x {1} = {2}'.format(n, 4, (n*4)))
print('{0} x {1} = {2}'.format(n, 5, (n*5)))
print('{0} x {1} = {2}'.format(n, 6, (n*6)))
print('{0} x {1} = {2}'.format(n, 7, (n*7)))
print('{0} x {1} = {2}'.format(n, 8, (n*8)))
print('{0} x {1} = {2}'.format(n, 9, (n*9)))
print('{0} x {1} = {2}'.format(n, 10, (n*10)))

#a mesma coisa que eu fiz lá em cima eu estou fazendo aqui.
#o nome tabuada vai ficar assim ---> '==tabuada=='  
print('{:=^30}'.format(t))
