#escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#o programa deverá escrever na tela se o usuário venceu ou perdeu.


#para criar esse programa, vou precisar importar a funcionalidade 'randint' da biblioteca 'math' (randint gera um número inteiro de forma aleatória)
from random import randint
#a funcionalidade sleep da biblioteca time, é só para gerar um suspense na hora de revelar o resultado final
from time import sleep

#aqui eu uso o randint para gerar um número inteiro de forma aleatória e depois armazeno o resultado em 'computer'
computer = randint(0, 5)
#para o programa ficar mais bonito, eu imprimo na tela os sinais '=-=' 30 vezes
print('=-=' * 25)
#agora eu aviso ao jogador que o computador 'escolheu' um número entre 0 e 5
print('Escolhi um número entre 0 e 5, tente adivinhar qual foi. ')
#e mais uma vez eu tento deixar o programa bonito, e imprimo na tela so sinais '=-=' 30 vezes
print('=-=' * 25)

#agora eu vou pedir para o jogador tentar adivinhar qual foi o número que o computador escolheu, e depois vou armazenar o resultado em 'player'
player = int(input('Digite o número que eu escolhi: '))
#para gerar um suspense, vou imprimir na tela a mensagem 'processando...' e vou usar a funcionalidade sleep da biblioteca time para fazer o programa
#esperar 3 segundos antes de revelar o resultado 
#>>  sleep(3) significa que eu estou pausando o computador por 3 segundos antes de dar continuidade ao programa. para isso eu faço:
#from time import sleep
# > sleep('quantidade de segundos')
# import time
# time.sleep('quantidade de segundos') 
print('PROCESSANDO...')
sleep(3)

#para o jogador vencer, ele precisa adivinhar qual foi o número que o computador escolheu. se ele acertar, vai imprimir na tela 'você ganhou'
if player == computer:
    print('Você ganhou, eu pensei no número {}'.format(computer))
#se o jogador errar, vai imprimir na tela que o jogador perdeu    
else:
    print('Você perdeu, eu pensei no número {} e não no número {}'.format(computer, player))
