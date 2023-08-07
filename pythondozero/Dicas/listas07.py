#diferentemente das tuplas, as listas podem ser modificadas...
#declarando listas[]
#toda lista fica entre os colchetes []
#posso declarar uma lista utilizando a função list() ou simplesmente utilizando os colchetes []
#usando os []

#exemplos 
#cria um lista chamada números e adiciona os valores 2 5 9 1
numeros = [2, 5, 9, 1]
#mostra os valores na tela 
print(numeros)
#dentro de numeros o elemento que está na posição 2 (o 9) vai passar a ser 3 
numeros[2] = 3
#mostra  numeros na tela com a substitução do segundo elemento da lista
print(numeros)
#pra adicionar um número na lista, eu uso a função append()
#obs: o metódo append adiciona o elemento no final da lista 
#adiciona o número 7 na lista numeros
numeros.append(7) 
print(numeros)

#ordenando os elemento da lista numeros com a função sort
numeros.sort() #o sort() ordena em ordem crescente
print(numeros)

#ordenando em ordem decrescente
#também uso a função sort(), mas passo o parâmentro reverse=True, veja abaixo
numeros.sort(reverse=True)
print(numeros) 

#usando a função len() para retorna a quantidade de elementos dentro da lista numeros
#o len() retorna o tamanho da lista

print(f'Essa lista tem {len(numeros)} elementos')


#inserindo elementos na lista 
#para inserir elementos dentro de uma lista eu uso a função insert('indico a posição', 'elemento que quero adicionar')
#ex
#dentro da lista numeros, na posição 2 eu vou inserir o elemento 0. e de forma automatica, 
#os elementos que estão a direita do elemento que eu vou inserir, deslocam para direita e reorganizam os seus indices
#ex:
print('inserindo elementos')
teste = [1, 2, 3]
print(teste)
teste.insert(1, 5)
print(teste)

print('removendo elementos')
#posso remover os elementos usando os metodos
#pop()
#remove()
#del

valores = [5, 3, 4, 6, 7]
print(valores)
#removendo com o del, basta digitar del dar um espaço digitar o nome da lista e indicar a posição:
#del nome_lista[posição]. veja abaixo
del valores[2]
print(valores)

valores = [5, 3, 4, 6, 7]
print(valores)
#removendo com a função pop(). quando eu não indico a posição, o pop remove o último elemento da lista.
#mas eu também posso indicar a posição do elemento que eu quero remover
valores.pop()#remove na ultima posição
valores.pop(0)#remove o elemento da posição 0
print(valores)

#removendo com a função remove
valores = [1, 0, 7, 3, 2, 5, 2 ]
print(valores)
#para eliminar um elemento da lista usando o remove eu não preciso indicar a posição, eu preciso indicar o valor
#por exemplo, para remover o elemento 2 eu não preciso indicar o indice(posição em que ele está). veja abaixo
valores.remove(2)
#obs, o metódo remove só elimina a primeira ocorrência, por isso que ele só eliminou um número 2
#ou seja, ele inicia procurando do primeiro elemento, o valor que você mandou eliminar e ele elimina a primeira ocorrência
#inicia na posição 0, vai até a primeira ocorrência do valor e elimina, mas eu posso usar os laços pra o remove
#fazer uma 'varredura' até o fim da lista do elemento que eu quero eliminar 
print(valores)
#outro exemplo com o remove
nomes = ['joão', 'ana', 'igor', 'jose']
print(nomes)
nomes.remove('jose')#remove o elemento que tiver o valor jose da lista nomes
print(nomes)

sobrenome = ['barbosa', 'souza', 'santos', 'oliveira']
if 'avelino' in sobrenome: #faz a verificação se existe 'avelino' dentro da lista sobrenome, se existe, faça
    sobrenome.remove('avelino') #remova o sobrenome avelino da lista
else: #senão
    #mostre um mensagem dizendo que não encontrou o sobrenome avelino
    print('não achei o sobrenome avelino na lista')



#adicionando valores em uma lista vazia
numbers = []
#adicionando os valores 2 1 6 0 na lista numbers
numbers.append(2) 
numbers.append(9)
numbers.append(6)
numbers.append(0)


#usando o enumerate eu posso mostra a posição e o elemento 
for posicao, numero in enumerate(numbers):
    print(f'adicionei o número {numero} na posição {posicao}')

for pos in range(0, len(numbers)):
    print(f'adicionei o elemento {numbers[pos]} na posição numero {pos}')

#declarando lista utilizando a função list()
#declarei a lista armazenei
armazenei = list()

for i in range(3):#inicio um laço for que vai repetir 3 vezes
    n = int(input('Digite um número:'))#a cada iteração pede pra o usuário digitar um número
    armazenei.append(n) #e depois adiciona o número que foi digitado na lista armazenei

print(armazenei)

#fazendo copia de listas
#dessa forma a alteração que eu faço na lista a, a lista b, sofre essa alteração também, 'elas criam uma ligação'
a = [1, 2, 3, 4, 5]
b = a #b recebe a lista a 
a[0] = 55 #na lista a, o elemento que tá na posição 0 vai ser substtituido por 55
b[2] = 8 #na lista b, o elemento que tá na posição 2 vai ser substtituido por 8

print(f'lista a {a}')
print(f'lista b {b}')

#pra esse problema não acontecer eu faço..
print('copiando do jeito certo')
a = [1, 2, 3, 4, 5]
b = a[:] #b recebe todos os elementos de a
 #dessa forma as listas não vão mais estar 'ligadas' a alteração que for feita em a, só vai ser feita em a
 #e do mesmo jeito pra b 
a[0] = 55 #na lista a, o elemento que tá na posição 0 vai ser substtituido por 55
b[2] = 8 #na lista b, o elemento que tá na posição 2 vai ser substtituido por 8

print(f'lista a {a}')
print(f'lista b {b}')
