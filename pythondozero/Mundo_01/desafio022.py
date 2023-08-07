#crie um programa que leia o nome completo de uma pessoa e mostre: 
# > o nome com todas as letras maiúsculas.
# > o nome com todas as letras minúsculas. 
# > quantas letras ao todo (sem considerar espaços). 
# > quantas letras tem o primeiro nome

#pede pra o usuário digitar um nome e armazena o resultado na variável 'nome'
#eu converti para str para especificar que é uma string e também já removi os espeços da direita e esquerda usando o strip()
#dessa forma a string já vai sair sem espaços indesejados tanto no lado direito como no esquerdo
nome = str(input('Digite o seu nome completo: ')).strip()

#o upper transforma toda a string em letra MAIÚSCULA e depois mostra o resultado na tela
print('O seu nome com letras maiúsculas é {}'.format(nome.upper()))

#o lower transforma toda a string em letra minúscula e depois mostra o resultado na tela
#OBS: eu estou transformando dentro da saida formatada para facilitar.
print('O seu nome com letras minúculas é {}'.format(nome.lower()))

#agora vou usar o split() para transformar a string que tá armazenada na variável 'nome' em uma lista
nome = nome.split()

#como eu transformei a string da variável nome em uma lista eu posso juntar um coisa na outra usando o join
#por exemplo:
#nome = 'joao igor'
#nome = nome.split()
#print(nome)
#>>> ['joao' , 'igor']
#como eu tô trabalhando com lista eu posso juntar a string dessa forma:
#nome = 'joao igor'
#nome = nome.split()
#print(''.join(nome))
#>>> joaoigor
#len(''.join.(nome[:])) >>> isso significa que len vai mostrar qual o comprimento(vai contar quantos caracteres tem na string) do inicio até o fim sem considerar os espaços
#relembrando
#len > mostra qual é o comprimento da string 
# [:] > como eu não defini o inicio da contagem, vai iniciar da posição 0 (primeiro caractere) e como eu não sei aonde termina,  vai até a ultima posição(até o ultimo caractere da string)
# ''.join(nome) > eu vou juntar a string(que tá armazenada em 'nome') utilizando esse separador ''(esse separado significa que não tem espaços). então eu estou removendo os espaços
print('O seu nome completo tem {} letras'.format(len(''.join(nome[:]))))

#agora eu vou mostrar na tela qual é o primeiro nome da pessoa. e para isso eu precisei transformar tudo que fosse armazenado em 'nome' numa lista pra depois pegar o primeiro nome[que fica na posição 0]
#e também vou mostrar na tela qual é o comprimento do primeiro nome da pessoa utilizando o len(nome[0])
print('O seu primeiro nome é {} e tem {} letras'.format(nome[0], len(nome[0])))

#eu também poderia fazer assim:

nome = str(input('Digite o seu nome completo: ')).strip()
#o upper transforma toda a string em letra MAIÚSCULA e depois mostra o resultado na tela
print('O seu nome com letras maiúsculas é {}'.format(nome.upper()))
#o lower transforma toda a string em letra minúscula e depois mostra o resultado na tela
#OBS: eu estou transformando dentro da saida formatada para facilitar.
print('O seu nome com letras minúculas é {}'.format(nome.lower()))
#aqui eu estou lendo o nome completo do usuário menos (-) a quantidade de espaços e depois vai mostrar na tela o comprimento da string sem considerar os espaços.
#para contar a quantidade de espaços use o .count(' ') 
print('O seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))

#eu posso usar o find para encontrar o primeiro espaço e encontrando o primeiro espaço já da pra saber o primeiro nome.
#funciona assim.
# nome = 'ana maria'
# print(nome.find(' '))
#>>> ana 
 # até o primeiro espaço são 4 caracteres, mas lembre - se que o ultimo número não é considerado então são 3 caracteres, ou seja, o primeiro nome é 'ana'
# em resumo o que tiver antes do primeiro espaço vai ser o primeiro nome.
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))