#faça um programa que leia um ano qualquer e mostre seele é BISSEXTO

#vou importar a funcionalidade 'date' da biblioteca 'datetime' para pegar o ano atual da minha máquina e analisar se é BISSEXTO  
from datetime import date

#começo o programa pedindo para o usuário digitar o que ele quer analisar e vou armazenar o resultado em 'ano'
#se o usuário digitar 0, o ano que vai ser analisado vai ser o ano atual
ano = int(input('Que ano quer analisar? Digite 0 para analizar o ano atual: '))

#vou criar a variável 'resultado' que vai analisar se o ano é ou não bissexto
#para saber se o ano é bissexto basta dividir o ano por 4 e depois pegar o resto da divisão por 4.
#vai ficar assim:
#(ano / 4) % 4 
resultado = (ano / 4) % 4 

#se o usuário digitou 0, o programa vai pegar o ano atual da máquina utilizando a funcionalidade date.today().year 
if ano == 0:
    ano = date.today().year

#se o resto da divisão do ano dividido por 4 for igual a 0, ele é bissexto, caso contrário ele não é bissexto
#agora imprima na tela se que foi digitado é ou não é bissexto.
if resultado == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} não é BISSEXTO'.format(ano))