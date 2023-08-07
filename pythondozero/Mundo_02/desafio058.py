#melhore o jogo do desafio028 onde o computador 'pensar' em número entre 0 e 10. só que agora o jogador
#vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

#estou importando somente a funcionalidade radint(escolher um número inteiro de forma aleatória) da biblioteca random
from random import randint
#estou importando somente a funcionalidade sleep(pausa o computador) da biblioteca time
from time import sleep

#pede uma entrada de dados do tipo str, elimina os espaços com o strip, joga tudo pra maiúsculo e pega o primeiro caractere
#depois armazena tudo em x
x = str(input('Eae, tá afim de jogar ? [S/N]')).strip().upper()[0]
# se o que foi armazenado em x tiver S maiúsculo ou s minúsculo faça:
if x in 'Ss':
    #mostra mensagem
    print('ok, vou pensar em número entre 0 e 10.')
    #pausa 1 segundo
    sleep(1)
    #mostra mensagem
    print('Estou pensando... aguarde!')
    #pausa 2 segundos
    sleep(2)
    #mostra mensagem
    print('Pensei!!! Tente adivinhar qual foi!')
    #uso o randint para escolher um número inteiro entre 0 e 10 de forma aleátoria 
    #e depois armazeno o resultado em computer
    computer = randint(0, 10)
    #agora peço um entrada de dado do tipo int e armazeno o resultado em palpite
    palpite = int(input('Qual é o seu palpite? '))
    #vou criar um contador, chamado tentativa para contar quantas vezes o usuário 
    #tentou antes de acertar qual foi o número que o computador escolheu. 
    # ele começa valendo 1 porque eu já pedi a primeira entrada de dado 
    tentativas = 1
    #se o meu palpite for diferente do computador, repita
    while palpite != computer:
        #se o meu palpite for maior que o número escolhido(computer) 
        if palpite > computer:
            #printe menos e pergunte qual é o meu palpite
            palpite = int(input('MENOS... tente mais uma vez! '))
            #incremento tentativa
            tentativas += 1
        #se o meu palpite for menor que o número escolhido(computer)
        if palpite < computer:
            #printe mais e pergunte qual é o meu palpite
            palpite = int(input('MAIS... tente mais uma vez! '))
            #incremente tentativa
            tentativas += 1
        #se o meu palpite for igual a do computador, mostre meu palpite, 
        # o número escolhido(computador) e o números de tentativas que eu precisei
        if palpite == computer:
            print("Parabéns, o seu palpite foi {} e o número escolhido foi {}. Na mosca!!".format(palpite, computer))  
    print("Acertou com {} tentativas!".format(tentativas))

    #se não estrou no primeiro if, mostre uma mensagem de despedida
else:
    print('Beleza então, tchau! (-_-)')







