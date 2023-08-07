#faça um programa que leia três números e mostre qual é o maior e qual é o menor 

#vou iniciar o programa pedindo 3 números ao usuário depois vou armazenar os resultados em n1, n2 e n3.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#para descobrir quem é o menor número vamos usar o 'and', para o and funcionar, as duas condições precisam ser verdadeiras, veja abaixo.
# if n1 < n2 and n1 < n3:
#    menor = n1
# se o n1 for menor que o n2 e o n1 for menor que o n3 significa que o n1 é o menor
# 
# if n2 < n1 and n2 < n3:
#    menor = n2
#se o n2 for menor que o n1 e o n2 for menor que o n3 significa que o n2 é o menor
#if n3 < n1 and n3 < n2:
#    menor = n3
#se o n3 for menor que o n1 e o n3 for menor que o n2 significa que o n3 é o menor

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#imprime na tela qual foi o menor número digitado
print('O menor número é {}'.format(menor))


#agora eu vou fazer a mesma coisa que eu fiz para descobrir quem era o menor número, o que vai mudar é o sinal. veja abaixo
# if n1 > n2 and n1 > n3:
#    maior = n1
# se o n1 for maior que o n2 e o n1 for maior que o n3 significa que o n1 é o maior
# 
# if n2 > n1 and n2 > n3:
#    maior = n2
#se o n2 for maior que o n1 e o n2 for maior que o n3 significa que o n2 é o maior
#if n3 > n1 and n3 > n2:
#    maior = n3
#se o n3 for maior que o n1 e o n3 for maior que o n2 significa que o n3 é o maior

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#imprime na tela qual foi o maior número digitado 
print('O maior número é {}'.format(maior))
