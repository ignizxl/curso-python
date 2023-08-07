# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

#crio um dicionário 
aluno = {}
#pede o nome, converte pra str e armazena em nome 
nome = str(input('Nome: '))
#pede a média do aluno, converte pra float e armazena em média  
media = float(input(f'Média de {nome}: '))
#se a média for maior ou igual a 7
if media >= 7:
    #situação recebe aprovado
    situacao = 'Aprovado'
#se a média estiver entre 5 e 6.9 (6.9 é menor que 7)
elif 5 <= media < 7:
    #situação recebe recuperação
    situacao = 'Recuperação'
else:
    #senão, situação recebe reprovado
    situacao = 'Reprovado'
#depois que tudo for armazenado eu vou adicionar no dicionário aluno
#crio a key 'Nome' e o value vai receber o que foi armazenado em nome 
aluno['Nome'] = nome
#crio a key 'Média' e o value vai receber o que foi armazenado em media
aluno['Média'] = media
#crio a key 'Situação' e o value vai receber o que foi armazenado em situacao 
aluno['Situação'] = situacao

print()
#crio um laço for, crio as variáveis key e values e uso a função items() 
# para pegar as keys e os values do dicionário
for key, values in aluno.items():
    #e a cada iteração eu mostro a key seguido do seu valor 
    print(f'{key} é igual a {values}')

print()
#eu também já posso pedir um valor e já adicionar na dicionário
#por exemplo

ficha = {}
#note que ao invés de criar uma variável simples, eu já crio uma key e peço uma entrada de dado pelo 
#pelo teclado e o que foi digitado vai ser o value 
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input('Média: '))

#se ficha na posição média for maior ou igual a 7
if ficha['Média'] >= 7:
    #crio a key situação e o seu value é aprovado
    ficha['Situação'] = 'Aprovado'
#se a média estiver entre 5 e 6.9 (6.9 é menor que 7)
elif 5 <= ficha['Média'] < 7:
    #crio a key situação e o seu value é recuperação
    ficha['Situação'] = 'Recuperação'
else:
    #crio a  key situação e o seu value é reprovado
    ficha['Situação'] = 'Reprovado'

#a função .items() pega as keys e os values 
#para cada key, e para cada value dentro de ficha.items(), faça
for key, values in ficha.items():
    #e a cada iteração eu mostro a key seguido do seu valor 
    print(f'{key} é igual a {values}')