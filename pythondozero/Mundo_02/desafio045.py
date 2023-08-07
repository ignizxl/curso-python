#crie um programa que faça o computador jogar jokenpô com você.

#vou começar importando a funcionalidade 'randint' da biblioteca 'random' para escolher um número inteiro de forma aleatória

from random import randint

#vou importar também a funcionalidade 'sleep' da biblioteca 'time' para pausar o computador por alguns segundos 
#para gerar um suspense na hora de revelar o resultado
from time import sleep

#vou mostrar na tela quais as opções que usuário pode escolher: pedra, papel ou tesoura
print('''Suas opções:
[0] - PEDRA 
[1] - PAPEL 
[2] - TESOURA ''')

#vou gerar um número aleatório entre 0 e 2 e vou armazenar o resultado em 'computer'
computer = randint(0, 2)

# se o número gerado for 0 é pedra e o resultado da escolha do computador 'rcomputer' recebe pedra
if computer == 0:
    rcomputer = 'PEDRA'
# se o número gerado for 1 é papel e o resultado da escolha do computador 'rcomputer' recebe papel
elif computer == 1:
    rcomputer = 'PAPEL'
# se o número gerado for 2 é tesoura e o resultado da escolha do computador 'rcomputer' recebe tesoura
elif computer == 2:       
    rcomputer = 'TESOURA'

#o rcomputer vai ser usado para imprimir na tela qual foi a jogada do computador 

#agora vou pedir para o usuário fazer a sua jogada e armazenar o resultado em 'player'
player = int(input('Qual é sua jogada? '))

# se o jogador escolher 0 ou 1 ou 2
if player == 0 or player == 1 or player == 2:
#para gerar um suspense, mostre na tela a mensagem 'processando'    
    print('PROCESSANDO')
# se o jogador escolheu 0, o resultado da escolha do player 'rplayer' recebe pedra
    if player == 0:
        rplayer = 'PEDRA'
#se o jogador escolheu 1, o resultado da escolha do player 'rplayer' recebe papel    
    elif player == 1:
        rplayer = 'PAPEL'
# se o jogador escolheu 2, o resultado da escolha do player 'rplayer' recebe tesoura   
    elif player == 2:
        rplayer = 'TESOURA'

# se a escolha do usuário for diferente de 0, 1 ou 2. mostre na tela opção de escolha inválida e depois saia do programa.
# quit() >>> sai do programa
else:
    print('Opção de escolha inválida. tente novamente!')
    quit()

#para gerar um suspense antes de revelar quem é o vencedor, vou usar a funcionalidade 'sleep' da biblioteca 'time' 
# para escrever jokenpô pausadamente 
sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(2)
print('PO!!!')

#agora vou escrever a 'results' na tela de forma centralizada entre sinais de '='
print('{:=^30}'.format(' Results '))

#vou mostra na tela qual foi a jogada do computador 'rcomputer' e qual foi a jogada do jogador 'rplayer'
print('O computador jogou {}\nO jogador jogou {}'.format(rcomputer, rplayer))

# se o computador jogou pedra e jogador jogou tesoura, jogador perde
if computer == 0 and player == 2:
    print('You lose')

# se o computador jogou tesoura e jogador jogou pedra, jogador ganha
elif computer == 2 and player == 0:
    print('You win')

#se o computador jogou papel e jogador jogou pedra, jogador perde
elif computer == 1 and player == 0:
    print('You lose')

# se o computador jogou pedra e jogador jogou papel, jogador ganha
elif computer == 0 and player == 1:
    print('You win')
#se o computador jogou tesoura e jogador jogou papel, jogador perde
elif computer == 2 and player == 1:
    print('You lose')

#se o computador jogou papel e jogador jogou tesoura, jogador ganha
elif computer == 1 and player == 2:
    print('You win')

#se o computador jogar o mesmo que o jogador, empate
else:
    print('DRAW!')

#imprima na tela 10 vezes os sinais '=-='
print('=-=' * 10) 



#fazendo de outra forma.


#vou criar a variável 'itens' e vou armazenar dentro dela as palavra 'pedra ', 'papel' e 'tesoura'.
#posição [0] = PEDRA 
#posição [1] = PAPEL 
#posição [2] = TESOURA

itens = ('PEDRA', 'PAPEL', 'TESOURA')

#vou pedir para o computador escolher um número de forma aleatória entre 0 e 2 e armazenar o resultado em 'computador'.
computador = randint(0, 2)

#vou mostra na tela as opções de jogadas do jogador 
print('''Suas opções:
[0] - PEDRA 
[1] - PAPEL 
[2] - TESOURA ''')

#vou pedir para o jogador fazer a sua jogada e armazenar o resultado em 'jogador'
jogador = int(input('Qual é a sua jogada ?\n '))


#para gerar um suspense antes de revelar quem é o vencedor, vou usar a funcionalidade 'sleep' da biblioteca 'time' 
# para escrever jokenpô pausadamente 

sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(2)
print('PO!!!')

#agora vou revelar os resultados.
print('=' * 11)

#vou mostra na tela a jogada do computador. format(itens[computador])) >>> o computador vai escolher um número e esse número vai indicar a posição de um dos 3 itens da lista
#ex: se o computador escolher 0, o que vai imprimir na tela vai ser pedra, porque pedra está na posição 0, se for 1, vai imprimir papel e se for 2, vai imprimir tesoura
#e funciona da mesma forma para o jogador.
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('=' * 11)

# e por fim, as condições


#computador pedra e jogador papel = jogador ganha
# computador pedra e jogador tesoura = jogador perde
# #mesma jogada = empate 
if computer == 0:
    if player == 1:
        print('You win')
    elif player == 2:
        print('You lose')
    else:
        print('DRAW!')

#computador papel e jogador pedra = jogador perde
#computador papel e jogador tesoura = jogador ganha
#mesma jogada = empate
elif computer == 1:
    if player == 0:
        print('You lose')
    elif player == 2:
        print('You win')
    else:
        print('DRAW!')

# computador tesoura e jogador pedra = jogador ganha
# computador tesoura e jogador papel = jogador perde
# mesma jogada = empate 

elif computer == 2:
    if player == 0:
        print('You win')
    elif player == 1:
        print('You lose')
    else:
        print('DRAW!')

print('=-=' * 10) 