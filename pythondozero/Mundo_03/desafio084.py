# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

#crio uma lista principal chamada 'pessoas' e crio um lista temporária chamada 'dados'
pessoas = list()
dados = list()
#crio dois acumuladores e ambos iniciam valendo 0.
maiorPeso = 0
menorPeso = 0
#crio um acumulador chamado c que vai servir apenas na primeira iteração do laço while
c = 0
#e crio também um acumulador chamado cadastrado
cadastrados = 0
#enquanto verdade, faça
while True:
    #peço o nome e o peso de uma pessoa e já adiciono dentro da lista temporária 'dados'
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    #depois copio tudo que foi armazenado dentro de dados e uso o append pra adicionar na lista pessoas 
    pessoas.append(dados[:])
    #se o meu contador for igual a 0, significa que é a primeira iteração, então o maior peso e o menor peso 
    #vão receber dados na posição 1 (posição 1 representa o peso)
    if c == 0:
        maiorPeso = dados[1]
        menorPeso = dados[1]
    #senão(apartir da segunda iteração vai cair no else)
    else:
        #faz a verificação, se dados na posição 1 for maior que o maior peso 
        if  dados[1] > maiorPeso:
            #maior peso recebe dados na posição 1
            maiorPeso = dados[1]
            #se dados na posição 1 for menor que o menor peso 
        if dados[1] < menorPeso:
            #menor peso recebe dados na posição 1 
            menorPeso = dados[1] 
    #depois eu preciso limpar a lista dados usando a função clear(), por isso que a lista dados é uma lista temporária
    #porque se eu não limpar a lista ela vai ficar acumulando e ela não pode acumular porque a cada iteração ela vai receber 
    #um dado novo, eu jogo na lista pessoas e depois limpo a lista dados e esse processo se repete 
    dados.clear()
    #incremento os contadores c e cadastrados 
    c += 1
    cadastrados += 1
    
    #crio uma variável chamada resposta que inicia como uma string vazia 
    resposta = ' '
    #enquanto resposta não estiver em 'SN', enquanto o usuário não digitar s ou n o while repete
    while resposta not in 'SN':
        #pede uma resposta, 'SN', elimina os espaçoes, joga a letra pra maiúscula e considera só a primeira letra
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    #se a resposta for igual a N, eu interrompo o laço while com o break 
    if resposta == 'N':
        break
#mostro a quantidade de pessoas que foram cadastradas
print(f'A quantidade de pessoas cadastradas foi {cadastrados}')
#mostro o maior peso que foi digitado e continuo na mesma pra imprimir na tela usando o laço for.
print(f'O maior peso registrado foi {maiorPeso}kg. Peso de ', end='')
#para cada pessoa dentro de pessoas, faça
for pessoa in pessoas:
    #se a pessoa na posição(posição 1 representa o peso) for igual o maiorPeso, eu mostro o nome da pessoa na tela
    #eu uso o laço for porque se tiver mais de uma pessoa com o mesmo peso, o nome dessa pessoa vai ser printado na tela
    if pessoa[1] == maiorPeso:
        print(f' [{pessoa[0]}]', end='')
print('.')
#e o mesmo processo se repete no laço abaixo, o for vai varrer toda lista pessoas e vai verificar se pessoa(represento o indice)
#for igual ao menor peso, mostre o nome da pessoa na tela 
print(f'O menor peso registrado foi {menorPeso}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menorPeso:
        print(f' [{pessoa[0]}]', end='')
print('.')


#outra forma de fazer 
#crio uma lista principal e uma lista temporária
principal = []
temp = []
menor = maior = 0 #ambos recebem 0
while True:
    #já adiciono a entrada de dado dentro da lista temporária
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    #faço a verificaçao se o tamanho da lista principal é igual a zero, se for
    #o maior e menor peso recebem temp[1] - >(representa o peso que foi lido)
    #esse if só vai funcionar na primeira iteração, porque logo depois da primeira iteração a lista principal já vai ter um item
    if len(principal) == 0:
        menor = maior = temp[1]
    else:
        #senão, se o temp[1] for maior do que o peso armazenado em maior,
        #maior recebe temp[1]
        if temp[1] > maior:
            maior = temp[1]
            #se o temp[1] for menor do que o peso armazenado em menor,
        #menor recebe temp[1]
        if temp[1] < menor:
            menor = temp[1]
    #faço uma cópia dos itens da lista temporária e adiciono na lista principal 
    principal.append(temp[:])
    #depois limpo a lista temporária pra ela não acumular 
    temp.clear()
    #pergunto se o usuário quer continuar, se a reposta for não eu interrompo o laço while com o break 
    resp = str(input('Quer continuar [N/S] '))
    if resp in 'nN':
        break
#pra mostra o número de pessoas cadastradas é só usar a função len na lista principal que vai me retornar o tamanho da lista, ou seja,
#o número de pessoas cadastradas 
print(f'Número de pessoas cadastradas {len(principal)}')
#mostro o maior peso lido e continuo na mesma linha. 
print(f'O maior peso foi de {maior}kg. Peso de ',end='')
#agora vou usar o laço for para varrer cada item da lista principal
for p in principal:
    #e faço a verificação, se o p[1] >> peso do primeiro item da lista for igual  a o peso armazenado em 'maior', mostre o nome da pessoa na tela 
    if p[1] == maior: #p[1] >>> peso da pessoa 
        print(f'[{p[0]}] ', end='') #p[0] >>> nome da pessoa 
print()
#e repito o mesmo processo aqui embaixo.
print(f'O menor peso foi de {menor}kg. Peso de ',end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')