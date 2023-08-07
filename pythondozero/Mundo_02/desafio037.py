#escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

#estou mostrando na tela os sinais '=-=' trinta vezes para tentar deixar o programa bonito
print('=-=' * 15)
#aqui estou mostrando na tela uma mensagem dizendo 'conversão de bases'
print('Conversão de Bases')
#e mais uma vez eu mostro 30 vezes os sinais '=-='
print('=-=' * 15)

#aqui eu peço para o  usuário digitar um número inteiro qualquer e depois armazeno o resultado em 'n'
n = int(input('Digite um número inteiro: '))

#depois peço para o usuário escolher a base de converção
# -1 para binário
# -2 para octal
# -3 para hexadecimal

#para não dar 3 print eu posso usar as 3 aspas para facilitar 
#print('''Escolha uma das bases para conversão:
#[ 1 ] converter para BINÁRIO 
#[ 2 ] converter para OCTAL 
#[ 3 ] converter para HEXADECIMAL''' )

print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO ')
print('[ 2 ] converter para OCTAL ')
print('[ 3 ] converter para HEXADECIMAL' )

#aqui o usuário digita qual o número da base de conversão >>> 1,2 ou 3 
op  = int(input('Sua opção: '))

#se o usuário digitar 1, eu uso a função interna do python 'bin' para converter o número digitado para binário
if op == 1:
    b = bin(n)
    #(b[2:]) >>> eu estou eliminando os 2 primeiros caracteres
    #e o começo da contagem  inicia do posição 2 e vai até o último caractere
    #os 2 primeiros caracteres é uma indicação de que está sendo convertido para binário, por isso que eu eliminei os 2 primeiros 
    print('{} convertido para BINÁRIO é {}'.format(n, b[2:]))

elif op == 2:
#se o usuário digitar 2, eu uso a função interna do python 'oct' para converter o número digitado para octal
    o = oct(n)
     #(o[2:])S >>> eu estou eliminano os 2 primeiros caracteres
    #e o começo da contagem inicia do posição 2 e vai até o último caractere
    #os 2 primeiros caracteres é uma indicação de que está sendo convertido para octal, por isso que eu eliminei os 2 primeiros 
    print('{} convertido para OCTAL é {}'.format(n, o[2:])) 
elif op == 3:
    h = hex(n)
     #(h[2:]) >>> eu estou eliminando os 2 primeiros caracteres
    #e o começo da  contagem inicia do posição 2 e vai até o último caractere
    #os 2 primeiros caracteres é uma indicação de que está sendo convertido para hexadecimal, por isso que eu eliminei os 2 primeiros 
    print('{} convertido para HEXADECIMAL é {}'.format(n, h[2:]))

    #se o usuário digitar uma opção diferente de 1,2 ou 3 vai aparecer uma mensagem dizendo que a opção selecionada não existe
else:
    print('O opção digitada não existe. teste o programa mais uma vez')