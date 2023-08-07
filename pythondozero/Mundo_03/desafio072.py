#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
#de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso.

#cria um tupla chamada numeros e preenche com os numeros de 0 a 20 por extenso
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#pede pra o usuário digitar um número entre zero e vinte, converte pra int e armazena em resp

resp = int(input('Digite um número entre 0 e 20: '))
#se o número digitado não estiver no intervalo
#entre 0 e 20, faça..
#ou, simplesmente posso apagar essa variável resp e esse if e identar a linha 16 até a 22 pra esquerda
#vai funcionar da mesma forma e em menos linhas 
if resp < 0 or resp > 20:
    #enquanto verdade...
    while True:
        #pede pra o usuário digitar novamente um número entre 0 e 20. enquanto o usuário não digitar o número entre 0 e 20 o while repete
        resp = int(input('Tente novamente! Digite um número entre 0 e 20. '))
        #se o número digitado estiver num intervalo entre 0 e 20, faça
        if resp >= 0 and resp <= 20:
            #interrompe o laço while com o break 
            break

#mostra a tupla que foi armazenada em numeros na posição resp
print(numeros[resp])

print('--------------------------------')

#outra forma de fazer 
#cria um tupla chamada numeros e preenche com os numeros de 0 a 20 por extenso
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#enquanto verdade..
while True:
    #pede pra o usuário digitar um número entre 0 e 20, converte pra int e armazena em resp
    resp = int(input('Digite um número entre 0 e 20: '))

    #se o número digitado estiver no intervalo entre 0 e 20
    if 0 <= resp <= 20:
        #encerre o laço while 
        break

    #se não atendeu o if acima, mostre a mensagem tente novamente e continue na mesma linha
    print('Tente novamente.', end=" ")


#mostre na tela o número digitado por extenso(numeros é a tupla e resp e a posição do elemento armazena na tupla numeros )
print(f'Você digitou o número {numeros[resp]}')





#cria um tupla chamada numeros e preenche com os numeros de 0 a 20 por extenso
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#enquanto verdade..
while True:
    #pede pra o usuário digitar um número entre 0 e 20, converte pra int e armazena em resp
    resp = int(input('Digite um número entre 0 e 20: '))

    #se o número digitado estiver no intervalo entre 0 e 20
    if 0 <= resp <= 20:
        #mostre na tela o número digitado por extenso(numeros é a tupla e resp e a posição do elemento armazena na tupla numeros )
        print(f'Você digitou o número {numeros[resp]}')
    
    else:
        #se não atendeu o if acima, mostre a mensagem tente novamente e continue na mesma linha
        print('Tente novamente.', end=" ")

    continuando = ' '
    while continuando not in 'SN':
        continuando = str(input('Quer continuar ? [S/N]')).strip().upper()[0]

        if continuando == 'N':
            break
        

