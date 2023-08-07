# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def linha():
    print('=-' * 20)

#criando a função maior que recebe vários números...
def maior(numeros):

    #pegando o maior valor e o tamanho de 'numeros'
    maiorValor = max(numeros)
    quantidade = len(numeros)

    print('Analisando os valores passados...')
    #uso um for para 'varrer' cada valor splitado dentro de num
    for i in numeros:
        #mostro o número e continuo na mesma linha
        print(f'{i}', end = ' ')
    #mostro a quantidade e o maior valor
    print(f'- Foram informados {quantidade} número(s) ao todo.')
    print(f"- O maior valor informado foi o número '{maiorValor}'.")

linha()
#chamo a função 'maior' e uso o split para 'fatiar' cada número digitado 
maior(input('Informe alguns números inteiros: ').split())
linha()

#outra forma de fazer 

#o sinal '*' indica que eu estou empacotando os parâmetros, ou seja, eu vou receber vários parÂmetros
def maiorValor(* numeros):
    
    linha()
    #criando um acumulador e a variável maior
    contador = maior = 0
    
    print('Analisando os valores passados...')
    #uso um for para percorrer cada número digitado
    for numero in numeros:
        #espera 2 seg, mostra o número e continua na mesma linha
        sleep(0.2)
        print(f'{numero} ', end = '', flush = True)

        #se for a primeira iteração do for, maior recebe número
        if (contador == 0):
            maior = numero
        #senão
        else:
            #se número for maior que 'maior'
            if (numero > maior):
                #maior recebe número
                maior = numero
        #incremento o contador
        contador += 1

    #mostro a quantidade de número digitados e o maior número
    print(f'- Foram informados {contador} número(s) ao todo.')
    print(f"- O maior valor informado foi o número '{maior}'.")

#chamo a função maior valor e passo alguns valores
maiorValor(2, 9, 4, 7, 1, 5)
maiorValor(3, 44, 5, 21, 1, 2)
maiorValor(1, 4, 6, 31, 1)