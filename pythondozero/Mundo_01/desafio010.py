#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# considere
# US$1.00 = R$3.27

#pede um número flutuante ao usuário e depois armazena em 'n'
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
n = float(input('Digite quantos reais você tem na carteira e veja quantos dólares você pode comprar. \n:R$ '))

#faz o calculo de real para dólar 
d = n / 3.27

#escreva na tela o número flutuante que o usuário digitou 
print('você possui R${:.2f}'.format(n))

#{:.1f} -> isso significa que só vai mostrar uma casa flutuante depois do ponto.
#por exemplo: 1.666 vai ficar ---> 1.6 (note que está apenas com uma casa flutuante depois do ponto)

#mostra na tela o resultado  da conversão 
print('R${:.2f} convertido para dólares >>> US${:.2f}'.format(n, d))
print('Você pode comprar US${:.2f}'.format(d))