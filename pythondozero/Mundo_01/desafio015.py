#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quias ele foi alugado. calcule o preço a pagar.
#sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

#pede a quantidade de dias alugados e depois armazena o resultado 'd'
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
d = float(input('Quantos dias alugados: '))
#pede os km rodados e armazena o resultado em 'km'
km = float(input('Quantos Km rodados: '))

#agora é só fazer o calculo. o enunciado diz que a cada dia alugado custa R$60.00
# e cada km rodado custa R$0.15
#sabendo disso é só multiplicar e depois somar.
# fica assim --> (dias alugados 'd' * 60) + (km rodado 'km' * 0,15)
#é necessário utilizar parênteses por causa da ordem de prescêdencia
t = (d * 60) + (km * 0.15)

#agora vamos mostrar na tela o resultado final, o total a pagar
print('Você alugou o carro por {0:.0f} dias e rodou {1:.2f}km. O total a pagar é R${2:.2f}'.format(d, km, t))