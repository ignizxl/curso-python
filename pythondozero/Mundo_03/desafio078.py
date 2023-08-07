#faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitador e as suas respectivas posições na lista.

#crio uma lista chamada numeros que inicia vazia
numeros = []

#uso o laço for para repetir 5 vezes 
for i in range(5):
    #pede uma entrada, converte pra int e armazena num
    num = int(input(f'Digite um número para a posição {i}: '))
    #depois uso o metódo append para adicionar o que foi armazenado em num na lista numeros
    numeros.append(num)
    #eu também posso adicionar na lista sem precisar criar essa variável simples chamada num
    #eu poderia fazer assim também:
    #
    #numeros.append(int(input(f'Digite um número para a posição {i}: ')))
    #dessa forma, eu já adiciono na lista sem precisar criar a variável



#mostra na tela os armazenado na lista numeros
print(f'Você digitou os valores {numeros}')
#uso a função max para pegar o maior armazenado dentro da lista numeros e depois armazeno em maior
maior = max(numeros)
#uso a função min para pegar o menor armazenado dentro da lista numeros e depois armazeno em menor
menor = min(numeros)
#mostro o maior valor digitado e as posições em que ele está
print(f'O maior valor digitado foi {maior} nas posições', end=' ')

#pra pegar as posições é simples, eu inicio um laço for num range que inicia do zero e vai até o tamanho da lista
for indice in range(0, len(numeros)):
    #agora eu faço a verificação, se o numeros(dentro da lista) na posição [indice] 
    # (indice indica a posição do elemento na lista) for igual a o maior (o que foi armazenado em maior)

    if numeros[indice] == maior:
        #mostre o indice na tela e continue na mesma linha 
        print(f'{indice}', end='..')
    
print()

print(f'O menor valor digitado foi {menor} nas posições', end=' ')
#pra pegar o posição do menor número funciona do mesmo jeito..
#inicio um laço for num range que inicia do zero e vai até o tamanho da lista
for indice in range(0, len(numeros)):
    #agora eu faço a verificação, se o numeros(dentro da lista) na posição [indice] 
    # (indice indica a posição do elemento na lista) for igual a o menor (o que foi armazenado em menor)
    if numeros[indice] == menor:
        #mostre o indice e continue na mesma linha 
        print(f'{indice}', end='..')
print()

#outra forma de fazer
#  
print('-=-' * 30)

#crio uma lista que inicia vazia 
lista_num = []
#crio dois acumuladores um chamador menornum e maiornum, ambos iniciam valendo 0
menor_num = 0
maior_num = 0
#crio um laço for que vai repetir 5 vezes
#o laço inicia no 0 e termina no 4
for i in range(0, 5):
    #não vou criar uma variável simples pra depois adicionar na lista
    #vou pedir uma entrada de dado, converter pra int e já vou adicionar(pra adicionar uso o
    # append) na listanum
    lista_num.append(int(input(f'Digite um número para a posição {i}: ')))

    #pra pegar o maior e menor numero da lista eu posso usar as funções min e max ou posso fazer desse outro jeito abaixp
    #se o indice i for igual a 0, significa que é a primeira iteração do for, então, o maior número e menor número recebe
    #o primeiro elemento que foi adicionado lista(lista_num[i] >>> o zero representa a primeira posição)
    if i == 0:
        #então menor e maior num recebem o primeiro número que foi adicionado na lista 
        menor_num = lista_num[i]
        maior_num = lista_num[i]
    #se o i não for mais igual a 0 significa que o for não está mais na primeira iteraçção, então faça
    else:
        #verifica se o que está na posição i da lista num é menor do que o número que foi armazenado 
        #em menor núm, se for, faça
        if lista_num[i] < menor_num:
            #menor num recebe lista num na posição i 
            menor_num = lista_num[i]
        
        #verifica se o que está na posição i da lista num é maior do que o número que foi armazenado 
        #em maior núm, se for, faça   
        if lista_num[i] > maior_num:
            #maior núm recebe lista num na posição i 
            maior_num = lista_num[i]
print('-=' * 30)
#mostra todos os valores que foram digitados e adicionados na lista num 
print(f'Você digitou os valores {lista_num}')
#mostra na tela qual foi o maior número digitado dentro da lista num e mostra as posições em que ele está
#e continuo na mesma linha 
print(f'O maior valor digitado foi {maior_num} nas posições: ',end=' ')
#agora vou pegar as posições em que o maior número aparece utilizando o laço for pra fazer 
#varredura na lista e verificar elemento por elemento 
#uso a função enumerate para numerar toda lista num 
for posicao, numero in enumerate(lista_num):
    #verifico se o numero(representa o primeiro elemento na primeira iteração, depois o segundo e por ai vai
    # até o fim da lista..) for igual a o maior num, faça
    #e posição representa posição 
    if numero == maior_num:
        #mostre na tela em que posição ele está
        print(f'{posicao}', end='..')
print()
#agora é só fazer a mesma coisa para o menor num
print(f'O menor valor digitado foi {menor_num} nas posições: ', end=' ')
# uso o laço for pra fazer uma 
#varredura na lista e verificar elemento por elemento 
#uso a função enumerate para numerar toda lista num

for posicao, numero in enumerate(lista_num):
    #verifico se o numero (numero representa o elemento) é igual a ao menor num, se for faça
    if numero == menor_num:
        #mostre na tela a posição em que ele está
        print(f'{posicao}', end='..')
print()