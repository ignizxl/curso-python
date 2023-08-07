# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#criando um dicionário chamado 'jogador' e uma lista chamada jogadores para armazena os dicionários
jogador = {}
jogadores = []

while True:
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

    #uso o append para enviar uma cópia do dicionário 'jogador' para lista 'jogadores'
    jogadores.append(jogador.copy())
    #depois eu uso o clear para limpar o dicionário 'jogador'
    jogador.clear()

    #faço o processo para validar a resposta do usuário 
    continuar = ' '
    while continuar not in 'SN':
        #pra resumir, enquanto o usuário não digitar 'N' ou 'S', o while repete 
        continuar = str(input('Deseja cadastrar um novo jogador ? [S/N]: ')).upper()[0]
        #se a resposta não for 'N' ou 'S', mostra um erro
        if (continuar not in 'SN'):
            print("Erro! Digite apenas 'S' para 'Sim' ou 'N' para 'Não'.")
    #ao fim do while, verifica se a resposta é igual a 'N', se for uso o break pra encerrar o laço 
    if (continuar == 'N'):
        break
    
print('=-=' * 30)
#criando uma 'tabela' simples para exibir os resultados '(:>15) alinhado a direitra em 15 espaços'
print(f'{"Cod":>3}   {"Nome":>7} {"Gols":>15} {"Total":>15}')
print('---' * 30)

#crio um for para percorrer cada jogador dentro da lista jogadores
for jogador in jogadores:
    #a cada iteração do for eu uso o index pra me retorna o indice do jogador e continuo na mesma linha 
    print(f'{jogadores.index(jogador):>3}', end = '')
    #e crio outro for para exibir os dados do jogador (nome, gols e total de gols) 
    for key, value in (jogador.items()):
        #eu preciso converte o 'value' pra str pra pode alinhar a saída 
        print(f'{str(value):>10}   ', end = " ") 
    print()

#enquanto verdade, faça 
while True:
    print('---' * 30)
    print('Deseja mostrar os dados de qual jogador ? (999 para encerrar):')
    #pede um número, converte pra int e armazena em opcao 
    opcao = int(input('Sua opção: '))

    #se opcao for igual a 999, eu o uso o break pra encerrar o lçao 
    if (opcao == 999):
        print('<< Encerrando >>')
        break
    #se opcao for maior ou igual o tamanho de jogadores ou menor que 0, mostro um erro 
    if (opcao >= len(jogadores) or opcao < 0):
        print("Opção inválida. Digite novamente!")

    #senão, faça 
    else: 
        #crio um laço for para percorrer cada jogador dentro de jogadores 
        for jogador in jogadores:
            #e a cada iteração do for, verifico se o indice do jogador da vez é igual a 'opcao' que é a 'chave
            #de busca' por assim dizer, se for, eu mostro o nome do jogador e faço o levantamento 
            if (jogadores.index(jogador) == opcao):
                print(f'-- Levantamento do jogador {jogador["Nome"].title()}')
                #como o jogador['gols'] é uma lista, eu uso o enumerate
                # e crio as variáveis 'partida' e 'gols' 
                for partida, gols in enumerate(jogador['Gols']):
                    #e a cada iteração, mostro a partida e gols da partida 
                    print(f'    => Na ª{partida + 1} partida, fez {gols} gols')


#outra forma de fazer
print() 
print('=-=-=- {} =-=-='.format('Segunda forma'))

#criando um dicionário e duas listas 
jogadorDeFutebol = {}
partidas = []
time = []

while True:
    #no inicio da iteração, limpo o dicionário
    jogadorDeFutebol.clear()

    #repetindo o mesmo processo da primeira solução ...
    jogadorDeFutebol['Nome'] = str(input('Nome do jogador: '))
    totPartidas = int(input(f'Quantas partidas o {jogadorDeFutebol["Nome"]} jogou? '))

    for i in range(1, totPartidas + 1):
        partidas.append(int(input(f"     Quantos gols na partida {i}? ")))
    #depois de adicionar os gols na lista 'partidas', faço uma cópia de todos os elementos e jogo na key 'gols'
    jogadorDeFutebol['Gols'] = partidas[:]
    #depois, para descobrir a soma de todos os gols, utilizo a função sun na lista partidas 
    jogadorDeFutebol['Total'] = sum(partidas)
    # mando uma cópia de 'jogadorDeFutebol' para a lista 'time' 
    time.append(jogadorDeFutebol.copy())
   
    #fazendo a validação da resposta 
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        #se a resposta for um 's' ou um 'n', o break encerra esse laço
        if (resposta in 'SN'):
            break
        print("Erro! Digite apenas 'S' ou 'N'.")
    
    #depois de validar a resposta, verifica se a resposta é igual a n, e se for, uso o break pra encerrar
    # o laço e partimos para exibição de resultados 
    if (resposta == 'N'):
        break

print('-=' * 30)

print('Cod ', end = '')
#crio um for para percorrer apenas as chaves do jogador (nome, gols e total)
for key in jogadorDeFutebol.keys():
    #e a cada iteração mostro a chave à esquerda em 15 espaços 
    print(f'{key:<15}', end = '')
print()

#crio um for para imprimir de maneira organizada
#codigo representa a iteração do for e o value é uma tupla com a key e o value correspondente
for codigo, value in enumerate(time):
    #mostro o código e continuo na mesma linha 
    print(f'{codigo:>3} ', end = '')
    #e crio outro for para pegar só os valores dentro de value
    for i in value.values():
        # alinhando o value em 15 espaços a esquerda (para alinhar eu preciso fazer a conversão para str)
        print(f'{str(i):<15}', end = '')
    print()

print('-=' * 30)

#e para imprimir o levantamento do jogador o processo é bem parecido com a solução anterior 
while True:
    chaveDeBusca = int(input('Mostrar levantamento de qual jogador? (999 encerra): '))

    if (chaveDeBusca == 999):
        break

    if (chaveDeBusca < 0 or chaveDeBusca >= len(time)):
        print(f"Erro! não existe jogador com o código '{chaveDeBusca}'. ")
        
    else:
        #time[chaveDeBusca]['Nome'] >>> dentro da lista 'time', no dicionário na posição 'chaveDeBusca'
        #pegue a key 'nome'
        print(f'--Levantamento do jogador {time[chaveDeBusca]["Nome"]}')
        #uso um for e um enumerate na key golst pra imprimir de maneira organizada
        for partida, gols in enumerate(time[chaveDeBusca]["Gols"]):
            #a cada iteração mostra o número da partida e os gols da partida 
            print(f'     >> Na {partida}ª partida, fez {gols} gols.')
    print('=-' * 30)
print('<< Encerrando >>')