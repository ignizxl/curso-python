#crie um programa onde o usuário possa digitar vários valores números e cadastre-os em uma lista. Caso o número já exista
#lá dentro da lista, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

#crio uma lista que inicia vazia   
numeros = []
#enquanto verdade, faça
while True:
    #pede uma entrada de dado, converte pra int e armazena em n 
    n = int(input('Digite um número: '))

    #verifica se o valor que foi armazenado em n já existe dentro da lista, se existir ele não vai adicionar 
    if n in numeros:
        print('Valor duplicado! Não vou adicionar')
    #senão, ele adiciona 
    else:
        #pra adicionar eu uso o metódo append
        numeros.append(n)
        print('Valor adicionado com sucesso...')

    #crio uma variável chamada continuar que inicialmente está como uma 'string vazia'
    continuar = ' '
    #enquanto continuar não estiver em SN, faça 
    while continuar not in 'SN':
        #pede uma entrada de dado, joga pra letra maiúscula,  elimina os espaços com o strip e 
        # pego só a primeira letra e depois armazena em continuar
        continuar = input('Quer continuar? [S/N]: ').upper().strip()[0]

    #se continuar for igual a N, uso o break pra interromper o laço while 
    if continuar == 'N':
        break
#depois mostra todos os valores que foram adicionados na lista em ordem crescente, pra ordenar eu uso 
#a função sorted
print(f'Você digitou os valores: {sorted(numeros)}')

print('-=' * 20)
#outra forma de fazer 

#usa função list pra declarar um lista, e armazena inicialmente está vazia 
valores = list()
while True: #enquanto verdade,faça 
    #pede uma entrada de dado, converte pra int e armazena em num
    num = int(input('Digite um número: '))
    #faz uma verificação se o que foi armazenado em num não existe dentro da lista valores, se não existir,
    #eu adiciono
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    #se já existir, eu não adiciono
    else:
        print('Valor duplicado. Não vou adicionar')
    
    #pergunta se o usuário quer continuar, joga a letra pra maiúscula, elimina os espaços com o strip e considera só a primeira letra
    #depois armazena tudo isso em resposta 
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]
    #se o que foi armazenado em resposta estiver em n, eu interrompo o laço while usando o break
    if resposta in 'N':
        break

print('=-' * 20)
#depois uso a função sort pra ordenar os valores em ordem crescente e depois mostro na tela.
valores.sort()
print(f'Você digitou os valores {valores}')