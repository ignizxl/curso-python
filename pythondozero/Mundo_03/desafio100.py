# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
# a soma entre todos os valores pares sorteados pela função anterior.


#importando a funcionalidade randint da biblioteca random 
from random import randint
#criando um lista chamda 'numeros' que inicia vazia 
numeros = []

#criando um função para sortear números aleatórios 
def sorteio():
    #sorteando um número aleatório de 1 a 10
    total = randint(1,10)

    #mostrando o total de valores que vão ser sorteados e continuo na mesma linha 
    print(f'Sorteando {total} valore(s) da lista: ', end = '')
    #crio um contador chamado 'i' que inicia valendo 0 
    i = 0
    #enquanto o 'i' for menor que 'total' (número sorteado de maneira aleatória)
    while i < total:
        #sorteia um número entre 1 e 20 e armazena em 'aleatorio'
        aleatorio = randint(1, 20)
        
        #se o número sorteado não estiver dentro da lista de números, faça
        if (aleatorio not in numeros):
            #adiciono o número na lista, mostro o número sorteado e continuo na mesma linha
            numeros.append(aleatorio)
            print(f'{aleatorio}', end = ' ')
            #e por fim, incremento o contador 
            i += 1
    print('FIM!')

#criando a função somandoPares que recebe um lista como parÂmetro
def somandoPares(lista):
    #crio um acumulador chamado somaDePares que inicia valendo 0
    somaDePares = 0
    #uso um for para percorrer cada elemento do lista 
    for i in lista:
        #e a cada iteração, verifico se o resto da divisão do i por 2 é igual a zero, se for, o número é par
        if (i % 2 == 0):
            #incremento o acumulador somaDePares com o i
            somaDePares += i
    #mostro a lista de números sorteados e a soma dos  pares 
    print(f"Somando todos os valores pares da lista: {lista}, temos {somaDePares}.")

#chamo as duas funções
sorteio()
somandoPares(numeros)

