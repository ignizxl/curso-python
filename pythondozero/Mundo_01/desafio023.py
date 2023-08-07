#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#exemplo:
#   digite um número: 1834
#   unidade:4
#   dezena:3
#   centena:8
#   milhar:1

#tem duas maneiras de resolver esse exercicio
#a primeira forma. com base em 4 números

#vou começar pedindo para o usuário digitar um número entre 0 a 9999 e vou armazenar o que ele digitar em 'n'

#n = int(input('Digite um número de 0 a 9999. \n'))

#agora vou converter tudo para str para facilitar 

#n = str(n)

#obs: essa primeira forma de fazer só funciona com 4 número se digitar apenas 1,2 ou 3 números vai dar errado
#como são 4 digitos, inicio a contagem. [0 1 2 3]. 
#sabendo disso, vamos localizar as posições da unidades, dezenas, centenas e milhar.
#relembrando. só funciona com 4 números. então vamos considerar que o usuário digitou 4 números
#a casa da milhar sempre é a primeira posição, ou seja, a posição 0
#a casa das centenas sempre é a segunda posição, ou seja, a posição 1
# a casa das dezenas sempre é a terceira posição, ou seja, a posição 2
# e a casa das unidades é sempre a ultima, ou seja, a posição 3 

#agora eu vou mostrar na tela a quantidade das unidades, dezenas, centenas e milhar dos 4 números digitado pelo usuário.

#print('unidade: {}'.format(n[0]))
#print('dezena: {}'.format(n[1]))
#print('centena: {}'.format(n[2]))
#print('milhar: {}'.format(n[3]))




#a segunda forma. forma matemática
#vou começar pedindo para o usuário digitar um número entre 0 a 9999 e vou armazenar o que ele digitar em 'n'
#como estamos trabalhando com números inteiro é necessário fazer a conversão para 'int'
n = int(input('Digite um número de 0 a 9999. \n'))

#unidade: de 0 a 9
#dezena: de 10 a 99
#centena: de 100 a 999
#milhar: de 1000 a 9999#

#para calcular as unidade eu vou fazer a divisão inteira de n por 1 e depois eu vou pegar o resto da divisão(pegar o resto da divisão é pegar o ultimo número).
# vai ficar assim: 
#>>> n // 1 % 10 --> eu pego 'n' divido por 1 depois divido por módulo de %10 (%10 vai pegar o resto da divisão, o ultimo digito)
#, esse resto vai ser a quantidade de unidades
u = n // 1 % 10

#para calcular as dezenas é da mesma forma, o que vai mudar é o seguinte, ao invés de dividir 'n' por 1, eu vou dividir 'n' por 10.
# vai ficar assim:
#>>> n // 10 % 10 --> divido n por 10 depois divido por % (10 e pega o resto da divisão)
d = n // 10 % 10

#é a mesma coisa. como se trata de centena. a centena vai de 100  a 999. então vamos dividir por 100.
#fica assim:
#>>> n // 100 % 10 
c = n // 100 % 10

#como a milhar é de 1000 a 9999 vamos dividir por 1000.
#fica assim:
#n // 1000 % 10
m = n // 1000 % 10


#agora vou exibir na tela a quantidade de unidades, dezenas, centenas e milhar.
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
