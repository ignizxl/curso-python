#faça um programa que leia a largura e altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

#pede pra o usuário digitar uma largura em metros e armazena em 'largura'
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
largura = float(input('Digite a largura da parede em metros: '))

#pede pra o usuário digitar uma altura em metros e armazena em 'altura'
altura = float(input('Digite a altura da parede em metros: '))

#o produto dos valores armazenados em 'largura' e 'altura' vai ser a área 
area = largura * altura

#'sabendo que cada litro de tinta, pinta uma área de 2m²' --> preste atenção no enunciado
#divindo a área por 2, vamos ter a quantidade de litros necessários para pintar a parede
litro = area / 2

#agora é só mostrar na tela as informações acima e o resultado dos calculos de área e litros necessário para pintar a parede.
print('A sua parede tem a dimensão de {0:.2f}x{1:.2f} e sua área é de {2:.4f}m².'.format(largura, altura, area))
print('Para pintar essa parede será necessário utilizar {0:.4f}L de tinta.'.format(litro))