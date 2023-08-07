#deselvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem.
#cobrando R$0,50 por cada km para viagens de até 200km e R$0,45 para viagens mais longas.

#vou começar pedindo a distância da viagem e vou armazenar o resultado em 'km'
km = float(input('Qual é a distância da sua viagem? \n Informe aqui:'))
#vai imprimir na tela uma mensagem dizendo que a mensagem vai começar 
print('Você está prestes a começar uma viagem de {0:.2f} km.'.format(km))

#agora vou calcular o preço da viagem, se 'km' for menor ou igual a 200, eu multiplico 'km' por 0.50. se km for maior que
#200, eu multiplico 'km' por 0.45

#existem duas formas de escrever as condições if e else com o que foi visto até agora. 
#a forma simplificada, que está escrita abaixo. particularmente eu não gosto, mas, funciona do mesmo jeito.
#preco = km * 0.50 if km <=200 else km * 0.45
 
#e existe a forma que eu  estou usando com mais frequência nos exercicios.
#forma escrita abaixo:  
if km <= 200:
    preco = km * 0.50 
else:
    preco = km * 0.45

#depois de calcular preço da passagem, agora vou imprimir na tela quanto que irá custar a passagem da viagem
print('E o preço de sua passagem será de R${0:.2f}'.format(preco))