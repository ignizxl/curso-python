#faça um programa que calcule a soma entre todos os números que 
#são múltiplos de três e que se encontram no intervalo de 1 até 500 

#a estou atribuindo o valor 0 a variável soma
soma =  0

# estou atribuindo o valor 0 a variável acumulador 
acumulador = 0

#laço de repetição entre o intervalo de 1  a 500 pulando de 2 em 2
for n in range(1, 501, 2):

    #se o resto da divisão de n por 3 for igual a 0 ele é um número múltiplo de 3
    if n % 3 == 0:
        # a soma vai receber o valor dela que inicialmente é 0, e vai somar com n
        # depois como o laço vai repetir, a soma vai somar o valor que foi armazenado 'n' + n e vai repetir esse processo até o final do laço
        soma = soma + n 

        #o acumulador é o mesmo esquema só que ao invés de somar o valor de 'n', ele está somando + 1.
        #ex: acumulador = 0
        # acumulador = acumulador + 1
        #achou um multiplo de 3
        #acumulador = acumulador(que agora vale 1) + 1
        #achou outro multiplo de 3 
        # acumulador = acumulador(que agora vale 2) + 1 
        # e assim por diante. vai repetir esse processo até chegar em 449 que é o ultimo número impar
        # lembrando que o acumulador só está contado os números que são multiplos de 3
        acumulador = acumulador + 1

# agora vou mostrar na tela a quantidade de valores solicitados e qual é o resultado da soma de todos os valores solicitados  
#(a quantidade de valores solicitados é a quantidade de números impares multiplos de 3 que existem entre 1 e 500) 
print('A soma dos {} valores solicitados é igual a {}'.format(acumulador, soma))
     



# soma += n >> é a mesma coisa que >> soma = soma + n 
# acumulador += 1 >> é a mesma coisa que  >> acumulador = acumulador + 1 
