#escreva um programa que converta uma temperatura digitada em C° e converta para °F

#pede para o usuário informar uma temperatura e depois armazena o resultado em 't'
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
t = float(input('Informe a temperatura em C°. \n: '))

#faz a conversão de graus °C para graus °F
# para isso eu preciso multiplicar o valor armazenado em 't' por 9/5 (que é 1.8) e depois somar tudo isso mais 32 
#vai ficar assim (t * 1.8) + 32
con = (t * 9/5) + 32

#e por fim, mostre os resultados da conversão de graus °C para graus °F 
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(t, con))