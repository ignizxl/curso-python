#crio um dicionário chamado pessoa, e crio a key nome e defino o valor 'joao igor', crio a key idade 
#e defino o valor 19 e crio também a key sexo e defino o valor masculino 
pessoa = {'Nome':'João Igor', 'Idade': 19, 'Sexo':'Masculino'}
print('mostrando na tela pessoa/key ')
#pessoa["Nome"] representa o value joão igor e pessoa["Idade"] representa o value 19
#obs:
print(f'{pessoa["Nome"]} tem {pessoa["Idade"]} anos. ')
print('mostrando só as keys do dicionário')
#a função keys() representa só as keys (Nome, Idade, Sexo)
print(pessoa.keys())
print('mostrando só os values do dicionário')
#a função values() representa só os values (joão igor, 19, masculino )
print(pessoa.values())
print()
#a usando a função items() funciona como a função enumerate que usamos nas listas e nas tuplas.
print('mostrando as keys e os values do dicionário')
#a função items() representa as keys e os values ('Nome':'João Igor', 'Idade': 19, 'Sexo':'Masculino')
print(pessoa.items())

#e usando a função items() eu posso mostrar as keys e os values usando o laço for
#para cada key e value em pessoas, faça
for key, value in pessoa.items():
    #mostre a key seguida do seu value
    print(f'{key} = {value}')

print()
print(pessoa)
print('vou remover o elemento sexo do dicionário')
#para remover um elemento do dicionário pessoa eu uso a função del e passo o nome do dicionário e a key entre 
#parenteses
del pessoa['Sexo']
print(pessoa)

print()
#crio um dicionário chamado estados usando a função dict
estados = dict()
#crio uma lista chamada brasil usanso a função list()
brasil = list()
#crio um laço for para repetir 3 vezes 
for i in range(0, 3):
    #a cada iteração do for eu crio uma key chamada uf dentro do dicionário estado e pede uma entrada de dado
    estados['uf'] = str(input('Unidade federativa: '))
    #e eu crio também outra key chamada sigla dentro do dicionário estado e pede outra entrada de dado
    estados['sigla'] = str(input('Sigla do Estado: '))
    #depois disso, eu adiciono uma cópia do dicionário na lista brasil
    #e pra pegar a cópia eu não posso usar o estados[:], no caso dos dicionários eu preciso usar a função 
    #copy()
    brasil.append(estados.copy())
#depois crio uma laço for para varrer cada dicionário dentro da lista brasil 
for estado in brasil:
    #e para cada valor dentro de estado(o objeto acima no primeiro laço for) eu uso a função values pra pegar só
    #os valores 
    for value in estado.values():
        #e a cada iteração do laço for eu mostro o value do estado.values e continuo na mesma linha 
        print(f'{value}', end=' ')
    print()



#ordenando dicionários

#importando as funções randint da biblioteca random, sleep da biblioteca time e itemgetter da biblioteca operator 
from random import randint
from time import sleep
from operator import itemgetter

#criando o dicionário 'jogadores'
jogadores = {}
#criando um laço for para repetir 4 vezes 
for i in range(1, 5):
    # a cada iteração eu uso o método randint da biblioteca random para 
    # sortear um número aleatório entre 1 e 6 e depois armazenar dentro de jogadores na key 
    # 'player{i}', onde o i representa o indice da vez
    jogadores[f'player{i}'] = randint(1, 6)
print('Valores sorteados: ')

#e crio outro for para exibir as key e os values
#a função items() retorna as keys e os values 
for key, value in jogadores.items():
    sleep(0.5)
    #a cada iteração mostra a key e o value correspondente
    print(f'O {key} tirou o valor {value} no dado')
print('=-=' * 10)
print('=-= Ranking dos Players =-=')
print()

#ordenando o dicionário 'jogadores' em ordem decrescente de acordo 
#com o value (o número sorteado aleatóriamente)

#pra isso, eu crio uma nova lista chamada 'ranking'
ranking = []
#ranking vai receber a função sorted com os parâmetros, jogadores.items() para pegar as keys e os values de jogadores,
#key = itemgetter(1) para pegar só os values (se for 0, pega as chaves e se for 1, pega os valores)
#e reverse = True para ordenar os values de forma decrescente 
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)

#criando um for para exibir na tela de maneira organizada 

#indice representando o indice da iteração do for 
#value representando uma tupla contendo a key e o value correspondente 
for indice, value in enumerate(ranking):
    #pausando 0.5 segundos a cada iteração 
    sleep(0.5)
    #como a iteração do for inicia do 0, eu coloquei indice + 1 para ficar 1 2 3 e 4
    #o value na posição 0 representa a key e o value na posição 1 representa o valor correspondente 
    print(f'{indice + 1}º lugar: {value[0]} com {value[1]}')
print()

#outra forma de fazer ...
# cont = 1
# for i in sorted(jogadores, key = jogadores.get, reverse = True):
#     sleep(0.5)
#     print(f'º{cont} lugar: {i} com {jogadores[i]}')
#     cont += 1 
# print()
