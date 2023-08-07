# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#criando um dicionário chamado 'jogador'
jogador = {}
#pede um nome, converte pra str, elimina os espaços da esquerda e da direita com o strip e armazena tudo na key 'Nome'
jogador['Nome'] = str(input('Digite o nome do jogador: ')).strip()
#criando a key 'Gols' que é uma lista 
jogador['Gols'] = []
#pede um número, converte pra int e armazena em partidasJogadas
#o title() é pra o primeiro caractere do nome inicianr com letra maiúscula
partidasJogadas = int(input(f'Quantas partidas o {jogador["Nome"].title()} jogou? '))
#criando um for para iniciar do 1 até o número de partidas jogadas + 1
for i in range(1, partidasJogadas + 1):
    #a cada iteração do for, pergunta quantos gols foram feitos na partida 'i' (indice da vez) e armazena na lista 
    #da key 'Gols'
    jogador['Gols'].append(int(input(f'     Quantos gols na {i}ª partida? ')))

#criando um acumulador chamado 'totalDeGols'
totalDeGols = 0
#criando um for para percorrer cada elemento da lista da key 'Gols'
for i in jogador['Gols']:
    # e a cada iteração o totalDeGols recebe += i(o elemento da vez)
    totalDeGols += i

#criando a key 'total de gols' com o value sendo 'totalDegols'
jogador['Total de Gols'] = totalDeGols

#mostrando da primeira forma 
print('=-=' * 20)
print(jogador)

#mostrando da segunda forma 
print('=-=' * 20)
#usando um for e a função items() para pegar as keys e os values 
for key, value in jogador.items():
    #a cada iteração, mostra a key e o value correspondente 
    print(f"a key '{key}' tem o value '{value}'")

#mostrando da terceira forma 
print('=-=' * 20)
print(f"O jogador {jogador['Nome']} jogou {partidasJogadas} partidas!")
#usando o enumerate para enumerar a lista da key 'gols'
for indice, gols in enumerate(jogador['Gols']):
    #o indice representa a partida e o gols representa os gols feitos nessa partida
    print(f'    => Na ª{indice+1} partida, fez {gols} gols')
    
#outra forma de fazer
print() 
print('=-=-=- {} =-=-='.format('Segunda forma'))

#criando um dicionário e uma lista 
jogadorDeFutebol = {}
partidas = []

#repetindo o mesmo processo da primeira solução ...
jogadorDeFutebol['Nome'] = str(input('Nome do jogador: '))
totPartidas = int(input(f'Quantas partidas o {jogadorDeFutebol["Nome"]} jogou?'))

for i in range(1, totPartidas + 1):
    partidas.append(int(input(f"     Quantos gols na partida {i} ?")))
#depois de adicionar os gols na lista 'partidas', faço uma cópia de todos os elementos e jogo na key 'gols'
jogadorDeFutebol['Gols'] = partidas[:]
#depois, para descobrir a soma de todos os gols, utilizo a função sun na lista partidas 
jogadorDeFutebol['Total'] = sum(partidas)

#para imprimir, o processo é o mesmo da primeira solução 

#primeira forma 
print('=-=' * 20)
print(jogadorDeFutebol)

#segunda forma 
print('=-=' * 20)
for key, value in jogadorDeFutebol.items():
    print(f'O campo {key} tem o valor {value}')

#terceira forma 
print('=-=' * 20)
print(f'Quantos gols o jogador {jogadorDeFutebol["Nome"]} jogou {totPartidas}!')
for partida, quantidadeDeGols in enumerate(jogadorDeFutebol['Gols']):
    print(f'   => Na partida {i}, fez {quantidadeDeGols} gols')
print(f'Foi um total de {jogadorDeFutebol["Total"]} gols')
print('=-=' * 20)