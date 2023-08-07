#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#ex: ana maria de souza
#primeiro = ana 
#último = souza

#pede um nome ao usuário, elimina os espaços da esquerda e da direita e depois armazena o resultado em 'nome'
nome = str(input('Digite o seu nome completo: ')).strip()
#agora eu crio a variável 'p' de primeiro nome, e jogo tudo que está armazenado em nome para dentro de uma lista e pego a posição 0 (que o primeiro nome)
p = nome.split()[0]
#agora eu crio a variável 'u' de ultimo nome, e jogo tudo que está armazenado em nome para dentro de uma lista e depois uso a metodo pop() para pegar o ultimo elemento de uma lista
u = nome.split().pop()


#agora eu mostro na tela uma mensagem, o primeiro e o ultimo nome 
print('Olá amigo, prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(p))
print('Seu segundo nome é {}'.format(u))

#segunda forma de fazer
#pede um nome ao usuário, elimina os espaços da esquerda e da direita e depois armazena o resultado em 'n'
n = str(input('Digite o seu nome completo: ')).strip()
#vou jogar o que foi armazenado em 'n' para dentro de uma lista e armazenar em 'nome'
nome = n.split()
#vou mostra na tela uma mensagem de boas vindas
print('Olá amigo, prazer em te conhecer!')
#para mostrar o primeiro nome basta digitar nome[0] para pegar o primeiro item da lista, ou seja, o primeiro nome
print('Seu primeiro nome é {}'.format(nome[0]))
#e para pegar o ultimo nome vamos usar o len para saber quantas posições tem 'nome', então eu posso fazer com que o programa me mostrar
# o nome na posição len de nome menos 1. o menos 1 é adicionado porque a contagem se inicia da posição 0# 
print('Seu segundo nome é {}'.format(nome[len(nome) - 1]))
