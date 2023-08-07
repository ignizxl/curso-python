# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

#criando a função factorial que recebe um número e um parâmetro show opcional
def factorial(numero, show = False):

    #docstring 

    """
    factorial(numero, show = False)
    -> Calcula o factorial de um número 
    :param numero: O número a ser calculado 
    :param show: (Opcional) Mostrar ou não a resolução
    :return: Retorna o valor do factorial de um número
    """

    #crio um contador chamado fact que inicia valendo 1
    fact = 1
    #e crio um contador chamado cont que inicia valendo 'numero'
    cont = numero
    #enquando o contador for maior que 0
    while cont > 0:
        #fact recebe fact vezes o contador 
        fact = fact * cont
        #verifica se o parâmetro opcional é igual a True, se for, faça  
        if (show):
            #verifica se o contador é igual a 'numero'
            if (cont == numero):
                #se for, mostra o valor do contador e continua na mesma linha 
                print(f'{cont}', end = '')
            else:
                #senão, mostra um x seguido do valor do contador e continua na mesma linha
                print(f' x {cont}', end = '')
        #e por fim, decrementa o contador 
        cont -= 1

    #ao fim do while, verifica se o parâmetro opcional é verdadeiro, se for retorna um sinal '=' seguido do 
    # valor de fact
    if (show == True):
        return f' = {fact}'
    #senão
    else:
        #retorna um o número que foi calculado e o valor do factorial 
        return f"O factorial de {numero} é '{fact}'."
    

#pede um número, converte pra int e armazena em n 
n = int(input('Deseja saber o factorial de qual número? '))
#pergunta se o usuário quer mostrar a resolução e armazena a resposta em show
show = input('Deseja mostrar a resolução? [S/N]: ').upper()[0]
#verifica se a reposta de show é igual a 'S', se for, faça
if (show == 'S'):
    #show recebe true
    show = True
#chama a função passando os parâmetros digitados acima
print(factorial(n, show))
#e no final mostra a documentação da função factorial 
print(factorial.__doc__)

print('=-' * 30)
#segunda forma de fazer 

def fact2(n, show = False):
    #docstrins
    
    """
    fact2(n, show = False)
    -> Calcula o factorial de um número 
    :param n: O número a ser calculado 
    :param show: (Opcional) Mostrar ou não a resolução
    :return: Retorna o valor do factorial de um número
    """
    
    #mesmo processo da solução acima
    #crio um contador chamado fact que inicia valendo 1
    fact = 1
    #crio um for pra inicia de 'n' e ir até o '0' retrocedendo de 1 em  1
    for i in range(n, 0, -1):   
        #verifica se show é verdadeiro 
        if (show):
            #mostra o i e continua na mesma linha 
            print(i, end = '')
            #verifica se o i é maior que 1 
            if (i > 1):
                #mostra o x e continua na mesma linha 
                print(' x ', end = '')
                
            else:
                #e na última iteração do laço, mostra um sinal de '='
                print(' = ', end = '')
        #fact recebe fact vezes o i 
        fact *= i
    #ao fim do for, retorna fact
    return fact

#pede um número, converte pra int e armazena em n 
n = int(input('Deseja saber o factorial de qual número? '))
#pergunta se o usuário quer mostrar a resolução e armazena a resposta em show
show = input('Deseja mostrar a resolução? [S/N]: ').upper()[0]
#verifica se a reposta de show é igual a 'S', se for, faça
if (show == 'S'):
    #show recebe true
    show = True

print(fact2(n, show))
print(fact2.__doc__)