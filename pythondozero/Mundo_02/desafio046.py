#faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#para ter uma pausa de 1 segundo entre eles vou importar a funcionalidade 'sleep' da biblioteca 'time'

#da bibliote time importe somente a funcionalidade sleep
from time import sleep

#agora vamos usar a estrutura de repetição for para fazer a contagem regressiva

#for > 'laço' | i > 'contador(variável de controle)' | range(10, 0, -1) > intervalo começando do 10 e terminando no 0 diminuindo de 1 em 1.
# ex: 10 - 1 = 9
#     9 - 1 = 8 
#     8 - 1 = 7 
#e assim por diante.

#'i' é uma variável de controle. então pra resumir eu vou fazer um laço pra eu contar no intervalo entre 10 e 0 
#se eu fizer assim:
#for i in range(10, 0, -1):
#a contagem começa no 10 e para no 1 porque sempre em um range o ultimo termo é ignorado. pra pegar o 0 eu uso o -1 dessa forma:

#a contagem inicia no 10 e para no 0 porque o -1 é ignorado, e vai voltando uma unidade
for i in range(10, -1, -1): 
#agora vai mostra a contagem regressiva de 10 até 0 pausando 1 segundo entre cada número
    print(i)
    sleep(1)
#quando o laço de repetição acabar, mostre na tela bum bum pow 
print('BUM! BUM! POW!')
