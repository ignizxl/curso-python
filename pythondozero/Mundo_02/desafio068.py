#faça um programa que jogue par ou impar com o computador. o jogo só será interrompido 
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele 
# conquistou no final do jogo.

#da biblioteca random eu importo somente a funcionalidade randint pra escolher um número de forma aleátoria
from random import randint
#estetica do programa, nada de importante..
print('=-' * 15)
print('Vamos jogar par ou ímpar')
print('=-' * 15)
#cada vez que o jogador vencer, o acumulador wins vai ser incrementado
wins = 0
#enquanto verdade 
while True:
    #escolhe um número entre 1 e 10 de forma aleátoria e armazena em computer 
    computer = randint(0, 10)
    #pede pra o usuário digitar um número e converte pra int 
    jogada = int(input('Digite um valor:'))
    #pede pra o usuário entre impar ou par, joga a letra pra maiúscula, elimina os espaços e considera apenas a primeira letra
    #  
    escolha = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    #se o usuário digitar errado, ou seja, qualquer coisa diferente de impar ou par.. faça 
    if escolha not in 'PpIi':
        #wnquanto verdade, faça.....
        while True:
            #pede pra o usuário entre impar ou par, joga a letra pra maiúscula, elimina os espaços e considera apenas a primeira letra
            escolha = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
            #se a escolhar for igual a p ou i, faça...
            if escolha == 'P' or escolha == 'I':
                #break para interromper o laço
                break

    #soma a o número que eu escolhi com o número escolhido pelo computador e armazena em soma
    soma = jogada + computer

    #se a escolha for igual a p, faça
    if escolha == 'P':
        #se o resto da divisão de soma por 2 for igual a zero, você venceu e deu par 
        if soma % 2 == 0:
            resultado = 'Você venceu!'
            pi = 'DEU PAR'
            #incremente contador wins
            wins += 1 
        else:
            #senão, você perdeu e deu impar 
            resultado = 'Você perdeu!'
            pi = 'DEU IMPAR'
        
    #se a escolhar for igual a I, faça
    elif escolha == 'I':
        #se o resto da divisão de soma por 2 for diferente de zero, você venceu e deu impar
        if soma % 2 != 0:
            resultado = 'Você venceu!'
            pi = 'DEU IMPAR'
            #incremente contador
            wins += 1
            #senão, você perdeu e deu par 
        else:
            pi = 'DEU PAR'
            resultado = 'Você perdeu!'
#mostro na tela a jogada do usuário, a do computador a soma das jogadas e digo se é par ou impar 
    print(f' Você jogou {jogada} e o computador {computer}. Total de {soma} {pi}')
    print('-='*15)
    #mostro o resultado
    print(f'{resultado}')
#se o resultado for igual a você venceu, o jogo continua
    if resultado == 'Você venceu!':
        print('Vamos jogar novamente...')
    #senão, mostre o tanto de vezes que eu venci e pare o programa.
    else:
        print(f'GAME OVER! Você venceu um total de {wins}')
        break


#outra forma de fazer

#vitorias vai ser incrementado cada vez que o jogador vencer do computador 
vitorias = 0 

#enquanto verdade faça.
while True:
    #pede um valor converte pra int e armazena em jogador 
    jogador = int(input('Diga um valor: '))
    #escolhe um número aleatório entre 0 e 10 e armazena em computador 
    computador = randint(0, 10)
    #total vai ser a soma de jogador + computador 
    total = jogador + computador

    #crio uma variável chamada tipo que é uma string vazia
    tipo = ' '
    #enquanto tipo não tiver um p ou um i, faça..
    while tipo not in 'PI':
        #pergunta ao usuário se ele impar ou par, elimina os espaços joga a letra pra maiúscula e pega só a primeira letra 
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        #mostra na tela a escolha do jogador e a do computador e a soma total, e por fim, continua na mesma linha 
    print(f'Você jogou {jogador} e o computador {computador}. total de {total} ', end='')
    #impria deu par se o resto de total por 2 for 0, senão, imprima deu impar 
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    
    #se o tipo for igual a p
    if tipo == 'P':
        #se o resto de total por 2 for par, você venceu! 
        if total % 2 == 0:
            print('você venceu!')
            #incremente contador 
            vitorias +=1
            #senão, você perdeu! e encerra o programa usando o break 
        else:
            print('você perdeu!')
            break
    
    #se a escolha for i
    elif tipo == 'I':
        #se o resto de total por 2 for diferente de 0, faça
        if total % 2 != 0:
            #você venceu, incremente contador vitórias 
            print('você venceu!')
            vitorias += 1
        
        #senão, vocÊ perdeu e encerra o programa 
        else:
            print('você perdeu!')
            break
    
    #se o jogador ganhou, ele continua jogando...
    print('Vamos jogar novamente ... ')
#ao final do laço mostre quantas vezes eu venci..
print(f'Game Over! Você venceu {vitorias} vezes.')
        
