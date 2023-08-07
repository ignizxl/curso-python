# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

#crio uma lista chamada matriz com 3 sublistas dentro dela
#matriz[0] >>> sublista 0 ou primeira linha da matriz
#matriz[1] >>> sublista 1 ou segunda linha da matriz
#matriz[2] >>> sublista 2 ou terceira linha da matriz

matriz = [[], [], []]
#crio uma contador chamado col que inicia valendo 0
col = 0
#inicio um laço que inicia na posição 0 e vai até o 8
for i in range(0, 9):
    #faz a verificação se o col for igual a 3, eu reseto o contador
    #a cada iteração o col vai indicar a posição da matriz que vai ser preenchida
    if col == 3:
        col = 0
    #se o indice i for menor ou igual a 2 eu adiciono o número digitado na sublista 0 e incremento o contador col
    if i <= 2:
        matriz[0].append(int(input(f'[0:{i}] : ')))
        col += 1
    #se o indice i for maior que 2 e menor ou igual a 5 eu adiciono o número digitado na sublista 1 e incremento o contador col
    elif i > 2 and i <= 5:
        matriz[1].append(int(input(f'[1:{i}] : ')))
        col += 1
    #senão, eu adiciono o número digitado na sublista 2 e incremento o contador col
    else:
        matriz[2].append(int(input(f'[2:{i}] : ')))
        col += 1
#mostro 3 vezez os sinais '=-='
print('=-=' * 3)
#e uso o for para mostra todos os valores de cada sublista 
for line in matriz:
    print(line)

print('=-=' * 3)
#pra deixar mais organizado eu vou imprimir cada elemento centralizado em 5 espaços 
# e faço isso para todos os elementos de cada sublista 
print('[{:^5}] [{:^5}] [{:^5}]'.format(matriz[0][0], matriz[0][1], matriz[0][2]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(matriz[1][0], matriz[1][1], matriz[1][2]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(matriz[2][0], matriz[2][1], matriz[2][2]))

print('=-=' * 3)
#outra forma de fazer

#crio uma lista chamada matriz3x3, e dentro de matriz3x3 eu crio outras 3 sublistas(cada sublista representa uma linha da matriz) e 
#dentro de cada sublistas eu coloco 3 zeros para ocupar as 3 posições da lista
#dessa forma eu não preciso usar o metódo append para adicionar um valor na lista, 
# eu só preciso substituir o valor digitado a para sua posição correspondente 
matriz3x3 = [[0,0,0], [0,0,0], [0,0,0]]
#crio um laço for para repetir 3 vezes, então para cada lines(linha)
for lines in range(0, 3):
    #eu crio outro laço de repetição para repetir 3 vezes, e é agora que eu vou começar adicionar os valores digitados em suas posições
    #correspondentes
    for cols in range(0, 3):
        #dentro da lista matriz3x3, dentro da sublista 0 e na posição da sublista 0, adicione o valor digitado pelo teclado, e esse processo 
        #vai ser repetido a cada repetição 
        matriz3x3[lines][cols] = int(input(f'Digite um valor para [{lines}, {cols}]: '))
print('-=' * 3)
#agora pra imprimir na tela eu vou usar o laço for mais uma vez repetindo 3 vezes 
for lines in range(0, 3):
    #agora eu vou mostrar na tela cada valor dentro da sublista, e pra isso, eu uso o for mais uma vez 
    for cols in range(0, 3):
        #mostra o valor centralizado em cinco espaços e continua na mesma linha 
        print(f'[{matriz3x3[lines][cols]:^5}]', end='')
    #e ao final do laço, eu uso um print vazio para 'quebrar a linha' e ficar organizado. se eu não fizer isso vai ficar todos os valores na mesma linha
    print()