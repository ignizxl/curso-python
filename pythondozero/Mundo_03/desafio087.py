#  Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

#crio uma lista chamada matriz com 3 sublistas dentro dela
#matriz[0] >>> sublista 0 ou primeira linha da matriz
#matriz[1] >>> sublista 1 ou segunda linha da matriz
#matriz[2] >>> sublista 2 ou terceira linha da matriz
matriz = [[], [], []]
#crio um acumulador chamado pares que inicia valendo 0 e crio um contador chamado col que também inicia valendo 0
pares = 0
col = 0
#crio um laço for que vai repetir 9 vezes 
for i in range(0, 9):
    #faço a verificação se o contador col é igual 3, se for o contador col vai ser 'resetado' e vai passar a valer 0
    if col == 3:
        col = 0
    #se o indice for menor ou igual a 2, eu tenho que adicionar os valores digitados na primeira linha da matriz(matriz[0]) 
    if i <= 2:
        #peço o valor e já adiciono dentro da matriz 
        matriz[0].append(int(input(f'[0:{col}] : '))) 
        #já faço a verificação se o número digitado é par, se ele for par eu já incremento o contador pares     
        if matriz[0][col] % 2 == 0:
            pares += (matriz[0][col])
        #incremento o contador col   
        col += 1
   #se o indice i for maior que 2 e menor ou igual a 5, eu preciso adicionar o valor digitado na segunda linha da matriz(matriz[1])
    elif i > 2 and i <= 5:
        matriz[1].append(int(input(f'[1:{col}] : ')))
         #já faço a verificação se o número digitado é par, se ele for par eu já incremento o contador pares com o número digitado
        if matriz[1][col] % 2 == 0:
            pares += (matriz[1][col])
        #incremento o contador col
        col += 1
   
    else:
        #senão
        matriz[2].append(int(input(f'[2:{col}] : ')))
        #já faço a verificação se o número digitado é par, se ele for par eu já incremento o contador pares com o número digitado
        if matriz[2][col] % 2 == 0:
            pares += (matriz[2][col])
        #incremento o contador col
        col += 1

#pego todos os valores da 3 coluna, somo tudo e armazeno o resultado da soma dentro de 'soma_col3'
soma_col3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
#pra pegar o maior valor da segunda linha eu uso a função max na matriz[1](representa a segunda linha da matriz)
maior_line2 = max(matriz[1])

print('=-=' * 8)
#mostro todos os valores da linha 1 2 e 3 centralizados em 5 espaços, eu também poderia usar um laço for para mostrar na tela 
print('[{:^5}] [{:^5}] [{:^5}]'.format(matriz[0][0], matriz[0][1], matriz[0][2]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(matriz[1][0], matriz[1][1], matriz[1][2]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(matriz[2][0], matriz[2][1], matriz[2][2]))
#mostro a soma dos pares, a soma ta col 3 e o maior valor da 3 linha 
print(f'A soma de todos os números pares digitados é {pares} ')
print(f'A soma dos valores da terceira coluna é {soma_col3} ')
print(f'O maior valor da segunda linha é {maior_line2} ') 

print()

#outra forma de fazer 

#crio uma lista chamada matriz3x3, e dentro de matriz3x3 eu crio outras 3 sublistas(cada sublista representa uma linha da matriz) e 
#dentro de cada sublistas eu coloco 3 zeros para ocupar as 3 posições da lista
#dessa forma eu não preciso usar o metódo append para adicionar um valor na lista, 
# eu só preciso substituir o valor digitado a para sua posição correspondente 
matriz3x3 = [[0,0,0], [0,0,0], [0,0,0]]
#crio os acumuladores da soma dos n pares, o maior valor da linha 2 e a soma da col 3, todos iniciam valendo 0
soma_dos_pares = maior_valor = soma_col3 = 0
#crio um laço for para repetir 3 vezes, então para cada lines(linha)
for lines in range(0, 3):
    #eu crio outro laço de repetição para repetir 3 vezes, e é agora que eu vou começar adicionar os valores digitados em suas posições
    #correspondentes
    for cols in range(0, 3):
        #dentro da lista matriz3x3, dentro da sublista 0 e na posição da sublista 0, adicione o valor digitado pelo teclado, e esse processo 
        #vai ser repetido a cada repetição 
        matriz3x3[lines][cols] = int(input(f'Digite um valor para [{lines}, {cols}]: '))
        #verifico se o número que foi digitado é par, se for eu incremento o contador soma dos pares 
        if matriz[lines][cols] % 2 == 0:
            soma_dos_pares += matriz[lines][cols] 
#agora pra imprimir na tela eu vou usar o laço for mais uma vez repetindo 3 vezes 
for lines in range(0, 3):
    #agora eu vou mostrar na tela cada valor dentro da sublista, e pra isso, eu uso o for mais uma vez 
    for cols in range(0, 3):
        #mostra o valor centralizado em cinco espaços e continua na mesma linha 
        print(f'[{matriz3x3[lines][cols]:^5}]', end='')
    #e ao final do laço, eu uso um print vazio para 'quebrar a linha' e ficar organizado. se eu não fizer isso vai ficar todos os valores na mesma linha
    print()
#mostro a soma dos pares 
print(f'A soma dos valores da pares é {soma_dos_pares}')
#crio um laço for para repetir 3 vezes, esse laço for só vai pegar os valores da terceira coluna que são:
# matriz[0][2]
# matriz[1][2]
# matriz[2][2]
for lines in range(0, 3):
    #o acumulador soma col 3 vai somar só os valores da col 3 
    soma_col3 += matriz[lines][2]
#mostro a soma da col 3
print(f'A soma dos valores da terceira coluna é {soma_col3}')
#agora vamos pegar o maior valor da segunda linha 
#pra isso eu vou criar um laço for que vai repetir 3 vezes e só vai fazer a verificação nos elementos da segunda
# linha 
for lines in range(0, 3):
    #se lines for igual a 0, é a primeira iteração do for e se é primeira iteração significa que é o primeiro elemento, então 
    if lines == 0:
        #maior valor vai receber o primeiro elemento da segunda linha(segunda sublista dentro da lista matriz3x3 ou matriz[1])
        maior_valor = matriz[1][lines]
    #senão, se, o matriz[1][lines](elemento da vez, varia depender da iteração do for) for maior que o valor armazenado em maior valor
    elif matriz[1][lines] > maior_valor:
        #maior valor recebe matriz[1][lines] 
        maior_valor = matriz[1][lines]
    #mostra o valor na tela 
print(f'O maior valor da segunda linha é {maior_valor}')