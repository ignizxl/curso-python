# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

#importando a funcionalidade 'sleep' da biblioteca 'time'
from time import sleep

#criando a função linha
def linha():
    #multiplo os sinais '-=' vezes 25 e armazeno tudo em 'line' 
    line = '-=' * 25

    #crio um for para percorrer cada sinal armazenado dentro de 'line' 
    for i in line:
        #a cada iteração do for, eu uso a função sleep para esperar 0.01 segundo antes de imprimir o 'i' 
        sleep(0.01)
        #mostro o 'i'(sinal), uso o end para continuar na mesma linha e uso também o flush = true
        #quando o 'flush' é true, a funcionalidade sleep vai funcionar da maneira que eu quero,
        #esperando 0.01 segundos e imprimindo o sinal a cada iteração do for, ou seja, a cada iteração
        #você vai ver uma 'linha' sendo formada como uma barra de 'loading'. Agora se o flush é false,
        #você não conseguie acompanhar essa linha sendo formada, você só vê o resultado final, que é 
        #a linha já foi toda 'formada', por assim dizer.
        # flush = true; a cada iteração do laço, 'espera' alguns segundos e printa o 'i'
        # flush = false; a cada iteração do laço, 'espera' alguns segundos mas não mostra o 'i', só mostra tudo
        # assim que o laço acabar 
        print(f'{i}', end = '', flush = True)
    print()

#crio a função 'contagem' que recebe como parâmetro, 'inicio', 'fim' e 'passo'
def contagem(inicio, fim, passo):
    #chama a função linha 
    linha()

    #verifico se o passo é negativo, se for, faça
    if (passo < 0):
        #eu multiplico o passo por -1 para transforma-lo em positivo 
        passo = passo * (-1)

    #se o passo for igual a zero, faça
    if (passo == 0):
        #passo recebe '1'
        passo = 1

    #se o fim for maior que o inicio, faça 
    if (fim > inicio):
        #contador recebe o inicio 
        contador = inicio
        #mostro uma mensagem e espero 1 seg
        print(f'Iniciando uma contagem de {inicio} até {fim} de {passo} em {passo}.')
        sleep(1)

        #enquanto o contador for menor ou igual ao fim
        while (contador <= fim):
            #eu repito o mesmo processo feito na função 'linha'
            #espero 0.5 seg e imprimo o contador 
            sleep(0.5)    
            print(f'{contador}' , end = ' ', flush = True)
            #como o fim é maior que o inicio, significa que eu estou 'avançando'
            #por isso eu incremento o contador com += passo 
            contador += passo
        
        print('FIM!')


    else:
        #repito o mesmo processo feito acima 
        contador = inicio

        print(f'Iniciando uma contagem de {inicio} até {fim} de {passo} em {passo}.')

        while (contador >= fim):
            
            sleep(0.5)   
            print(f'{contador}' , end = ' ', flush = True)  
            #mas, como aqui o inicio é maior que o fim, significa que eu estou 'retrocedendo'
            #por isso eu decremento o contador com -= passo 
            contador -= passo

        print('FIM!')
        #e por fim, chamo a função linha 
        linha()


#chamo a função e passo alguns valores
contagem(1, 10, 1)
contagem(10, 1, 1)

#e por fim, pede pra o usuário fazer um contagem personalizada
print('Defina uma contagem personalizada!')
inicio = int(input('Inicio: '))
fim    = int(input('Fim: '   ))
passo  = int(input('Passo: ' ))
#chama a função contagem, passando os valores definidos pelo usuário
contagem(inicio, fim, passo)



# def contagemPersonalizada(inicio, fim, passo):
    
#     if (passo == 0):
#         passo = 1 

#     if (inicio > fim and passo > 0):
#         passo = passo * (-1)
    
#     if (inicio < fim and passo < 0):
#         passo = passo * (-1)

#     for i in range(inicio, fim + 1, passo):
#         print(f'{i}', end = ' ')
    
#     print('FIM!')



# def contador():

#     print('=-' * 20)
#     print('Contagem de 1 até de 10 de 1 em 1!')
#     for i in range(1, 10 + 1):
#         #sleep(0.5)

#         print(f'{i}', end = ' ')
        
#     print('FIM!')
    
#     print('=-' * 20)

#     print('Contagem de 1 até de 10 de 2 em 2!')
#     for i in range(10, -1, -2):
#         #sleep(0.5)

#         print(f'{i}', end = ' ')
        
#     print('FIM!')
    
#     print('=-' * 20)

#     print('Agora é a sua vez de personalizar a contagem!')
#     inicio = int(input('Digite o inicio: '))
#     fim = int(input('Digite o fim: '))
#     passo = int(input('Digite o passo: '))

#     contagemPersonalizada(inicio, fim, passo)

# contador()