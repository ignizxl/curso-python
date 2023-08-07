#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#mostrando na tela 12 sinais '=' para decoração
print('='* 12)

#pede pra o usuário digitar um valor e depois armazena o que foi digitado em 'preco'
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
preco = float(input('Qual é o preço do produto? \n:R$'))

#calcule 5% de desconto do valor que foi digitado em 'preco'
#o novo preço vai ser o preço antigo menos o 5% 
# preço antigo = (preco)
# desconto = (preco * 5/100)
# novo preço = preco - (preco * 5/100) 
novo_preco = preco - (preco * 5/100)

#mostre na tela qual vai ser o desconto do valor armazenado em 'n'(o que o usuário digitou)
print('O produto que custava R${:.2f} , na promoção com 5% de desconto vai custar apenas R${:.2f}'.format(preco, novo_preco))
