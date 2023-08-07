#crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.


#vou começar pedindo para o usuário digitar alguma frase, uso o 'strip()' para eliminar os espaços da esquerda e da direita
# e uso o upper() para transformar tudo que foi digitado em letra maiúscula e depois vou armazenar tudo em 'frase'
#estou especificando que estou trabalhando com uma string(por isso converto para str) 
frase = str(input('Digite uma frase:')).strip().upper()

#agora vou pegar a frase digitada e vou deixar ela splitada, a frase vai ser 'fatiada' ex:
# frase = 'joao igor'
# palavras = frase.split()
# print(palavras)
# saida >>> ['joao'], ['igor']  
palavras = frase.split()

#agora vou juntar toda frase, sem espaços.
#pra isso eu uso o ''.join(palavras), eu vou juntar tudo com ''(sem espaços). 
#em vez das palavras sairem de forma esplitadas ex: ['joao'] ,['igor'], agora elas vão sair assim: joaoigor 
tudojunto = ''.join(palavras)

#o contrario não tá recebendo nada
contrario = ''

#para reescrever a frase digitada da direita para esquerda, eu posso usar o for, ou essa forma de tratamento de string
# o contrario ta recebendo tudo junto na posição [:: -1] >>> significa que vai da posição inicial(0) até a posição final (ultimo elemento)
# voltando de 1 em 1
# contrario = tudojunto
#contrario = tudojunto[:: -1]

#agora vou criar um laço de repetição for
#vai começar do tamanho do len de tudojunto -1(ultimo elemento), (o ultimo termo é ignorado) até a posição -1
# (na verdade vai até o '0' porque o ultimo termo é ignorado), voltando de 1 em 1 (por isso o '-1')
for letra in range(len(tudojunto) - 1, -1, -1):

#o contrario ta recebendo contrario(nada) + tudojunto[letra] (tá recebendo tudojunto da direita para esquerda < ex:>>> igor | <<< rogi
    contrario = contrario + tudojunto[letra]

#agora eu vou imprimr na tela a tudojunto(frase escrita normal sem espaços) e contrario(frase escrita da direita para esquerda e sem espaços)
print('O inverso de {} é {}'.format(tudojunto, contrario))

# se tudojunto for igual a contrario, mostre na tela 'é um palindromo'
if tudojunto == contrario:
    print('É um palindromo')

#senão, mostre na tela, 'não é um palindromo'
else:
    print('A frase digitada NÃO é um palindromo')





#sem usar o for 

#vou começar pedindo para o usuário digitar alguma frase, uso o 'strip()' para eliminar os espaços da esquerda e da direita
# e uso o upper() para transformar tudo que foi digitado em letra maiúscula e depois vou armazenar tudo em 'frase'
#estou especificando que estou trabalhando com uma string(por isso converto para str) 
frase = str(input('Digite uma frase:')).strip().upper()

#agora vou pegar a frase digitada e vou deixar ela splitada, a frase vai ser 'fatiada' ex:
# frase = 'joao igor'
# palavras = frase.split()
# print(palavras)
# saida >>> ['joao'], ['igor']  
palavras = frase.split()

#agora vou juntar toda frase, sem espaços.
#pra isso eu uso o ''.join(palavras), eu vou juntar tudo com ''(sem espaços). 
#em vez das palavras sairem de forma esplitadas ex: ['joao'] ,['igor'], agora elas vão sair assim: joaoigor 
tudojunto = ''.join(palavras)

#para reescrever a frase digitada da direita para esquerda, eu posso usar o for, ou essa forma de tratamento de string
# o contrario ta recebendo tudo junto na posição [:: -1] >>> significa que vai da posição inicial(0) até a posição final (ultimo elemento)
# voltando de 1 em 1
# contrario = tudojunto
contrario = tudojunto[:: -1]

#agora eu vou imprimr na tela a tudojunto(frase escrita normal sem espaços) e contrario(frase escrita da direita para esquerda e sem espaços)
print('O inverso de {} é {}'.format(tudojunto, contrario))

# se tudojunto for igual a contrario, mostre na tela 'é um palindromo'
if tudojunto == contrario:
    print('É um palindromo')

#senão, mostre na tela, 'não é um palindromo'
else:
    print('A frase digitada NÃO é um palindromo')    