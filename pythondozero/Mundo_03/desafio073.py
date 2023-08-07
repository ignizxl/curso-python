#crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, 
#na ordem de colocação. depois mostre:
#a-) os primeiros 5
#b-) os últimos 4 colocados.
#c-) times em ordem alfabética
#d-) em que posição está o time da chapecoense

#cria uma tupla com os vinte primeiros times do brasileirão 2018
equipes = ('Corinthians', 'Palmeiras','Santos', 'Grêmio',
        'Cruzeiro', 'Flamento', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo' , 'Fluminense', 'Sport Recife', 'EC Vitória',
        'Coritiba', 'Avai', 'Ponte Preta', 'Atlético-GO')


print('-=' * 30) #esse print é só para separar as linhas e melhorar a aparência do programa
#lista todos os times do brasileirão que estão armazenado dentro da tupla equipe
print(f'Lista de times do Brasileirão: {equipes}')
print('-=' * 30)
#mostra os 5 primeiros times que estão dentro da tupla equipe.
# (equipes[0:5] >>> dentro da tupla equipe, inicie no elemento 0 e termine no elemento 5 e printe esses elementos)
print(f'Os 5 primeiros são: {equipes[0:5]} ')
print('-=' * 30)
#dentro da tupla equipe, inicia no elemento -4 e termine no ultimo elemento da tupla e printe esses elementos
print(f'Os 4 últimos são: {equipes[-4:]}')
print('-=' * 30)
#utilizo a função sorted na tupla equipe para imprimir os times em ordem alfabética 
print(f'Times em ordem alfabética: {sorted(equipes)}')
print('-=' * 30)
#utilizo a função index para indicar a posição da chapecoense e no final somo + 1 porque a contagem inicia no 0
#equipes.index('nome do elemento que deseja saber a posição')
print(f"O Chapecoense está na {equipes.index('Chapecoense') + 1}ª posição ")
