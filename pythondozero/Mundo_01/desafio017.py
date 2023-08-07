#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa

#pede uma entrada de dado, converte pra float e armazena em ca
ca = float(input('comprimento do cateto oposto: '))
#pede uma entrada de dado, converte pra float e armazena em co
co = float(input('comprimento do cateto adjascente: '))
#calculando a hipotenusa. basta elevar o cateto oposto e o adjacente a 2, e depois pego tudo isso e elevo a 1/2
hi = (co ** 2 + ca ** 2) ** (1/2)
#agora é só printar na tela a saida formatada com duas casas decimais, {:.f e a quantidade de casas}
print('A hipotenusa vai medir {:.2f}'.format(hi))

# importando a biblioteca math
#da biblioteca math eu importo somente a funcionalidade hypot para calcular a hipotenusa
from math import hypot

#pede uma entrada de dado, converte pra float e armazena em ca
ca = float(input('comprimento do cateto oposto: '))
#pede uma entrada de dado, converte pra float e armazena em co
co = float(input('comprimento do cateto adjascente: '))
#calculando a hipotenusa. basta elevar usar a funcionalidade hypot da biblioteca math
hi = hypot(ca,co)
#agora é só printar na tela a saida formatada com duas casas decimais, {:.f e a quantidade de casas}
print('A hipotenusa vai medir {:.2f}'.format(hi))
