#faça um algoritmo que leia o salário de um funcionário e mostre seu novo saláro, com 15% de aumento.

#mostrando na tela 12 sinais '=' para decoração
print('='* 12)

#pede pra o usuário digitar um valor e depois armazena o que foi digitado em 's'
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
s = float(input('Qual é o salário do funcionário? \n:R$'))

#calcule 15% de aumento do valor que foi digitado em 's'
#o salário com aumento vai ser o salário antigo(s) mais 15% (s * 15/100) 
# salário antigo = (s)
# aumento = (s * 15/100)
# salário com aumento = s + (s * 15/100) 
a = s + (s * 15/100)

#mostre na tela o salário antigo  (o que o usuário digitou) e o salário com aumento (o salário antigo mais os 15%)
print('O salário de R${:.2f} , com um aumento de 15% vai ficar R${:.2f}'.format(s, a))



# s = float(input('Qual é o salário do funcionário? \n:'))
# a = s + (s * 15/100)
# print('aumento',a) 