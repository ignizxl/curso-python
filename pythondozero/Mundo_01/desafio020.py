#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.



#eu estou importando apenas a funcionalidade 'shuffle'(embaralhar) da biblioteca 'random'
from random import shuffle

#agora eu vou pedir para o usuário digitar o nome de 4 alunos e armazenar o resultado nas variáveis a1,a2,a3 e a4.
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

#
# agora eu vou jogar as todas as variáveis(a1,a2,a3,a4) dentro de uma lista e armazenar tudo dentro da variável 'l'.
l = [a1, a2, a3, a4]
#agora eu vou usar a funcionalidade shuffle para embaralhar todos os itens que estão dentro da lista
#como eu estou importando de forma especifica eu não preciso digitar o random.shuffle(l), só precisa digitar shuffle(l)
shuffle(l)

#agora eu vou mostra na tela o resultado do embaralhamento da lista
print('A ordem de apresentação é:')
print(l)