#crie um programa que leia o ano de nascimento de sete pessoas. 
#no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#vou começar importando a funcionalidade 'date' da biblioteca 'datetime' pra pegar o ano atual da minha máquina
#pra isso eu uso o date.today().year
from datetime import date

#aqui eu vou atribuir o date.today().year a variável anoatual
anoatual = date.today().year

#vou criar um acumulador chamado de 'dmaior'
dmaior = 0
#e vou criar outro acumulador chamado de 'dmenor'
dmenor = 0

#vou criar um laço de repetição começando do número e vai até o número 7
for i in range(1, 8):
    #vou pedir a data de nascimento de 7 pessoas e vou calcular a idade delas
    nasc = int(input('Digite o ano de nascimento da {} ªpessoa: '.format(i)))
    #para calcular a idade, basta subtrair o ano atual pelo ano de nascimento da pessoa
    idade = anoatual - nasc

    #os acumuladores vão funcionar da seguinte forma:
    #se a idade da pessoa for maior ou igual a 21, o 'dmaior' recebe 'dmaior'(0) + 1 e o laço repete novamente.
    #pra resumo, se a idade for maior ou igual a 21, o dmaior soma +1, e vai acumulando se o if acontecer  
    if idade >= 21:
        dmaior += 1
    #se entra no else(idade < 21), o 'dmenor' recebe 'dmenor'(0) + 1 e o laço repete novamente.
    #pra resumo, se entrar no else, o dmenor soma +1, e vai acumulando se o else acontecer  
    else:
        dmenor += 1

#agora vou mostra quantas pessoas são maiores de idade(o que foi acumulado em dmaior) e quantas são menores(o que foi acumulado em dmenor)
print('Ao todo tivemos {} pessoas maiores de idade \n e também tivemos {} pessoas menores de idade'.format(dmaior, dmenor))
