#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
#como eu não estou convertendo o input, o tipo primitivo sempre vai ser 'str'

#pede pra o usuário digitar algo e depois armazena em n
n = input('Digite algo: ')

#mostra algumas informações sobre  o que foi armazenado em 'n' ( o que foi digitado no input acima)
print(f'O tipo primitivo é {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanúmerico? {n.isalnum()}')
print(f'Está em maiúscula? {n.isupper()}')
print(f'Está em minúscula? {n.islower()}')
print(f'Está capitalizado? {n.istitle()}')

#o 'n' é um objeto. todo objeto tem caracteristicas e realiza funcionalidades, eles tem atributos e metódos.
#no exemplo acima, observer que como tem um parênteses depois de cada um deles 'por ex: n.isspace()' , estamos trabalhando metódos  
#todos objeto string tem esses metódos 

#print('existem outras informações, mas eu só mostrei essas 4, por enquanto')

