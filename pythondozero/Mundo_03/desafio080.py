#Crie um programa onde o usuário possa digitar cinco valores numéricos e 
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

#crio uma lista chamada ordenando que inicia vazia e vai sendo preenchida cada vez que o usuário digitar
#um número
ordenando = []
#crio um laço for que inicia no zero e vai até o número 4.
for indice in range(5):
    #pede um número, converte pra int e armazena em numero
    n = int(input())
    #faz a verificação, se o indice for igual a zero ou se o número digitado for maior que o último elemento da lista
    #numeros_ordenados[-1] -> representa o último elemento da lista 
    if indice == 0 or n > ordenando[-1]:
        #depois adiciono o número digitado no fim da lista (o append por padrão já adiciona no final da lista)
        ordenando.append(n)
        print('Adicionado no final da lista')
   #senão
    else:
        #crio um contador (esse contador vai funcionar como um indice de um laço for)
        posicao = 0
        #enquanto o meu contador posição for menor que o tamanho da lista, faça
        while posicao < len(ordenando):
            #se o número digitado for menor ou igual ao elemento da lista na posição 'posicao',faça
            if n <= ordenando[posicao]:
                 #vou inserir o número na posição 'posicao' utilizando a função insert 
                ordenando.insert(posicao, n)
                print(f'adicionado na posição {posicao}')
                #e por fim uso o break pra interromper o laço while 
                break
            #a cada iteração eu incremento o o contador posição 
            posicao += 1
#e por fim mostro a lista ordenada
print(ordenando)



#crio uma lista chamada numeros_ordenados que inicia vazia e vai sendo preenchida cada vez que o usuário digitar
#um número
numeros_ordenados = []
#crio um laço for que inicia no zero e vai até o número 4.
for indice in range(5):
    #pede um número, converte pra int e armazena em numero
    numero = int(input('Digite um número: '))
    #faz a verificação, se o indice for igual a zero ou se o número digitado for maior ou igual a o último elemento da lista
    #numeros_ordenados[-1] -> representa o último elemento da lista 
    if (indice == 0 or numero >= numeros_ordenados[-1]):
        #depois adiciono o número digitado no fim da lista (o append por padrão já adiciona no final da lista)
        numeros_ordenados.append(numero)
        print('adicionando no final da lista')
    #senão, faça
    else:
        #crio um contador (esse contador vai funcionar como um indice de um laço for)
        posicao = 0
        #enquanto o meu contador posição for menor que o tamanho da lista, faça
        while posicao < len(numeros_ordenados):
            #se o número digitado for menor ou igual ao elemento da lista na posição 'posicao',faça
            if(numero <= numeros_ordenados[posicao]):
                #mostre na tela em que posição o número está sendo adicionado 
                print(f'adicionando na posição {posicao}')
                #vou inserir o número na posição 'posicao' utilizando a função insert 
                numeros_ordenados.insert(posicao, numero)
                #e por fim uso o break pra interromper o laço while 
                break
            #a cada iteração eu incremento o o contador posição 
            posicao += 1
#e por fim mostro a lista ordenada 
print(f'Sua lista ordenada é {numeros_ordenados}')