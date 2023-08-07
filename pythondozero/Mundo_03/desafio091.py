#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#importando as funções randint da biblioteca random, sleep da biblioteca time e itemgetter da biblioteca operator 
from random import randint
from time import sleep
from operator import itemgetter

#criando o dicionário 'jogadores'
jogadores = {}
#criando um laço for para repetir 4 vezes 
for i in range(1, 5):
    # a cada iteração eu uso o método randint da biblioteca random para 
    # sortear um número aleatório entre 1 e 6 e depois armazenar dentro de jogadores na key 
    # 'player{i}', onde o i representa o indice da vez
    jogadores[f'player{i}'] = randint(1, 6)
print('Valores sorteados: ')

#e crio outro for para exibir as key e os values
#a função items() retorna as keys e os values 
for key, value in jogadores.items():
    sleep(0.5)
    #a cada iteração mostra a key e o value correspondente
    print(f'O {key} tirou o valor {value} no dado')
print('=-=' * 10)
print('=-= Ranking dos Players =-=')
print()

#ordenando o dicionário 'jogadores' em ordem decrescente de acordo 
#com o value (o número sorteado aleatóriamente)

#pra isso, eu crio uma nova lista chamada 'ranking'
ranking = []
#ranking vai receber a função sorted com os parâmetros, jogadores.items() para pegar as keys e os values de jogadores,
#key = itemgetter(1) para pegar só os values (se for 0, pega as chaves e se for 1, pega os valores)
#e reverse = True para ordenar os values de forma decrescente 
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)

#criando um for para exibir na tela de maneira organizada 

#indice representando o indice da iteração do for 
#value representando uma tupla contendo a key e o value correspondente 
for indice, value in enumerate(ranking):
    #pausando 0.5 segundos a cada iteração 
    sleep(0.5)
    #como a iteração do for inicia do 0, eu coloquei indice + 1 para ficar 1 2 3 e 4
    #o value na posição 0 representa a key e o value na posição 1 representa o valor correspondente 
    print(f'{indice + 1}º lugar: {value[0]} com {value[1]}')
print()

#outra forma de fazer ...
# cont = 1
# for i in sorted(jogadores, key = jogadores.get, reverse = True):
#     sleep(0.5)
#     print(f'º{cont} lugar: {i} com {jogadores[i]}')
#     cont += 1 
# print()
