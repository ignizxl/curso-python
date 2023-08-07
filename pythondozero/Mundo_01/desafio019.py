#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# faça um programa que ajude ele, lendo o nome delas e escrevendo o nome do escolhido.

#eu estou importando apenas a funcionalidade 'choice'(escolha aleatória) da biblioteca 'random'
from random import choice

#agora eu vou pedir para o usuário digitar o nome de 4 alunos e armazenar o resultado nas variáveis a1,a2,a3 e a4. 
# o input já converte tudo para string, mas eu também posso fazer a conversão para string
#ficaria assim >>> str(input('Nome do aluno: '))
#eu estou convertendo uma string para string. por isso não é obrigatório, você converte para str se você quiser. é opcional
 
a1 = input('Nome do 1° aluno: ')
a2 = input('Nome do 2° aluno: ')
a3 = input('Nome do 3° aluno: ')
a4 = input('Nome do 4° aluno: ')

# agora eu vou jogar as variáveis(a1,a2,a3,a4) dentro de uma lista e armazenar tudo dentro da variável 'l'.
#é importante destacar que os itens de uma lista devem ficar entre [] conchetes e, se tiver mais de um item, eles devem ser separados por ','
#veja abaixo
l = [a1, a2, a3, a4]
#depois crio a variável 's' e eu uso a funcionalidade choice para sortear 1 dos 4 itens da lista (variável 'l') 
s = choice(l)
#agora mostre na tela quem foi o sorteado da lista.
#o que vai mostrar na tela vai ser o valor armazenado da variável que foi escolhida e apenas o sorteado da lista.
#ex:
#se eu digitar 'ana' no nome do primeiro aluno, o nome 'ana' vai ser armazenado na variável 'a1', correto?
#se o 'a1' for o sorteado da lista, o que vai mostra na tela vai ser o valor que foi armazenado em 'a1', ou seja, vai mostra na tela o nome 'ana' 
#  
print('O aluno sorteado foi {}'.format(s))
