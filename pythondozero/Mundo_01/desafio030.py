#crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

#vou começar pedindo para o usuário digitar um número inteiro qualquer e depois vou armazenar o resultado em 'n'
n = int(input('Digite um número qualquer:'))
#para saber se o número é par, basta pegar o resto da divisão de 'n' por 2 e ver se o resultado é igual a 0, se for 0 o número é par.
#se for 1, o número é impar
# = --> é atribuição
# == --> é comparação
#aqui eu já fiz o calculo dentro do if, também não tem problema, a não ser que eu precise desse resultado depois.
if  n%2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))

#segunda forma de fazer 

#vou começar pedindo para o usuário digitar um número inteiro qualquer e depois vou armazenar o resultado em 'n'
n = int(input('Digite um número qualquer:'))
#vou ver se o número que foi digitado é par ou impar e depois vou armazenar o resultado dentro da variável 'resultado'
#para saber se o número é par, basta pegar o resto da divisão de 'n' por 2 e ver se o resultado é igual a 0, se for 0 o número é par.
#se for 1, o número é impar.
resultado = n % 2

#agora eu vou comparar se o valor da variável resultado é igual a 0. se for igual a 0, imprime par. caso contrário, imprime impar.
if  resultado == 0:
     print('O número {} é par'.format(n))
else:
     print('O número {} é ímpar'.format(n))