# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

#importo a funcionalidade sample da biblioteca random
#O sample() retorna uma lista com uma seleção aleatória de um número especificado de itens de uma sequência.
from random import sample
#importo a funcionalidade sleep da biblioteca time 
from time import sleep
#crio uma lista chamada palpites
palpites = []

#pede um número, converte pra int e armazena em njogos
njogos = int(input('Quantos jogos deseja sortear? '))
#inicio um laço for do 1 e termina no número que foi armazenado em 'njogos'
for i in range(1, njogos+1):
    #uso a funcionalidade sample pra gerar 6 números aleatórios de 1 a 60 e depois adiciono tudo na lista palpiltes
    palpites.append((sample(range(0,60), int(6))))

#crio um contador chamado n que inicia valendo 1
n = 1
#crio um laço for para varrer todas as sublistas dentro de palpites
for i in palpites:
    #para cada sublista dentro de palpites, faça
    #mostro o valor de n(representando o jogo) e mostre a sublista(representado os 6 números) 
    print(f'Jogo {n}: {i}')
    #incremento o contador n 
    n += 1
    # e faço uma pausa de 1 segundo antes da próxima iteração do for 
    sleep(1)
#no fim do laço eu mostro um boa sorte 
print('<<< Boa sorte! >>>')

#outra forma de fazer 
print()

#importo a funcionalidade randint da biblioteca random
from random import randint 
#crio duas lista, uma temporária e outra para armazenar os jogos 
lista_temporaria = list()
jogos = list()
#pede um número, converte pra int e armazena em quantidade_jogos
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
#crio um contador chamado total que inicia valendo 1(se eu iniciar esse contador do 0 ele vai fazer um jogo amais, por isso inicio do 1)
total = 1
#enquanto o meu contador total for menor ou igual a quantidade de jogos, faça
while total <= quantidade_jogos:
    #crio um contador que incia valendo 0
    contador = 0
    #enquanto verdade, faça
    while True:
        #uso a funcionalidade randint para gerar um número aleatório entre 1 e 60 e depois eu armazeno em num
        num = randint(1,60)
        #se o número aleatório que foi armazenado em num não existir dentro da minha lista temporária, faça
        if num not in lista_temporaria:
            #eu adiciono o que foi armazenado em num na lista temporária
            lista_temporaria.append(num)
            #e incremento o contador 
            contador += 1
        #se o contador for maior ou igual a 6, encerro o laço com o break
        if contador >= 6:
            break
    #uso a função sort para ordenar os valores da lista
    lista_temporaria.sort()
    #envio uma cópia da lista temporária para a lista jogos 
    jogos.append(lista_temporaria[:])
    #limpo a lista temporária 
    lista_temporaria.clear()
    #e incremento o contador total
    total += 1
#para imprimir na tela eu uso um laço for e uso também a função enumerate na lista jogos 
#o i representa o meu indice(posição) e o l representa o meu jogo(a sublista dentro da lista jogo)
for i, l, in enumerate(jogos):
    #espero 1 segundo
    sleep(1)
    #mostro o resultado do sorteio
    print(f'Jogo {i+1}: {l}') 
print('<<< Boa sorte! >>>')
