#escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior 
# - não existe valor maior, os dois são iguais

#vou começar pedindo o primeiro número ao usuário e depois vou armazenar o resultado em 'n1'
n1 = int(input('Digite o primeiro número: '))
#depois vou pedir o segundo número e vou armazenar o resultado em 'n2'
n2 = int(input('Digite o segundo número: '))

#agora é só comparar o 'n1' com o 'n2'
#se o 'n1' for maior que o 'n2' escreva 'o primeiro valor é maior'
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n1 < n2:
#se o 'n1' for menor que o 'n2' escreva 'o segundo valor é maior'
    print('O SEGUNDO valor é maior.')
#e se 'n1' não for maior que 'n2', e 'n1' não for menor que 'n2' eles só podem ser iguais. 
# então como não existe uma quarta opção, eu já uso o else.
else:
    print('Não existe valor mair, os dois valores são iguais.')