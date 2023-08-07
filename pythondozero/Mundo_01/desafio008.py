#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

#peça um número ao usuário e armazene o resultado em 'm'
#como estamos trabalhando com metros sabemos que podem ter situações em que o usuário vai digitar 1,5 metros por exemplo, e 1.5 não é  um número inteiro, é um número flutuante(real)
#por este motivo que a conversão deve ser feita para float
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
#pergunte uma distância ao usuário e depois converta para float e armazene o resultado em 'm'. é basicamente isso que eu estou dizendo para o computador  
m = float(input('Digite um distância em metros: '))

#faça os calculos de conversão: 
# metros pra centimetro(multiplique por 100)
# metros pra milimetro (multiplique por 1000)
# quilômetro (divida por 1000)
cent = m * 100
mil = m * 1000
km = m / 1000

#mostre na tela os resultados dos calculos feitos acima

print('{0} metros para centimetros --> {1:.0f} cm'.format(m, cent))
print('{0} metros para milimetros --> {1:.0f} mm'.format(m, mil))
print('{0} metros para quilômetros --> {1:.2f} km'.format(m, km))

#{:.0f} --> significa que eu não quero nenhuma casa flutuante depois do ponto.
#{:.2f} --> significa que eu quero apenas duas casas flutuantes depois do ponto.
# por exemplo: 1.666666
# com casa flutuante depois do ponto --> 1.666666 
# sem casa flutuante depois do ponto --> 1
# com duas casas flutuantes depois do ponto --> 1.66 



#converti o resultado de 'cent' e 'mil'(que estão em float) para int só para tentar deixar o código organizado 
# print(f'{m} metros para centimetros --> {int(cent)} centimetros')
# print(f'{m} metros para milimetros --> {int(mil)} milimetros')
# print(f'{m} metros para quilômetros --> {km} quilômetros')

