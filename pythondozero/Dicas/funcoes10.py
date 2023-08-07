# funções/ rotinas 

#declarando uma função em python
#basta usar a palavra reservada 'def' seguida do nome da função e depois abre e fecha parênteses 
#obs: dentro dos parênteses você pode passar parâmetros

#exemplo: def 'nomeDaFuncao'('nomeDaVariavel'):

#exemplo prático

#criando um função chamada 'soma' que recebe 2 parâmetro (a e b)
def soma(a, b):
    #depois soma o valor de 'a' + o valor de 'b' e armazena em 'resultado' 
    resultado = a + b
    #e depois de ter calculado, printa o resultado
    print(resultado)
    print(f"O resultado da soma entre o valor de A = '{a}' + o valor de B '{b}' é igual a '{resultado}'")

#chama a função 'soma' passando 10 e 4 como parâmetro 
soma(10, 4)

#eu posso especificar quem é o valor de a e que é o valor de b
soma(a = 4, b = 10)

#'empacotando parâmetros'
# empacotar parâmetros, é passar uma quantidade indeterminada de parâmetro na função
#para empacotar os parâmetros basta colocar um '*' antes do nome da variável
def contadorDeNumeros(* variosNumeros):
    #uso a função len para contar quantos números foram passador como parÂmetro
    quantidadeDeNumeros = len(variosNumeros)
    #exibe os resultados
    print(f'Quantidade de números informados: {quantidadeDeNumeros}')
    print(f'Os números informados foram: {variosNumeros}')

#chamo a função e passo alguns números 
contadorDeNumeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def dobrandoValores(listaDeNumeros):

    print(f'Lista de números antes: {listaDeNumeros}')
    #criando um for para percorrer cada elementro dentro da lista de números 
    for i in range(0, len(listaDeNumeros)):
        #e a cada iteração do for, lista de números na posição i eu multiplico por 2 
        listaDeNumeros[i] *= 2
    
    print(f'Lista de números depois: {listaDeNumeros}')
numeros = [1, 2, 3, 4, 5]
dobrandoValores(numeros)


#ajuda iterativa
#help('comando') 
#ex: help(print)

#segunda forma de usar a ajuda iterativa
#print(print.___doc__) >>> vai imprimir toda documentação do comando print

#docstrings e escopo de importação
#docstrings são strings de documentação e elas são exibidas durante a ajuda iterativa
#ex:



def linha():
    #note que ao invés de fazer a importação a importação para o programa inteiro,
    #eu faço a importação apenas dentro da função linha(), dessa forma eu economizo memória. 
    #Então como eu só preciso utilizar a função sleep dentro da função linha(), eu só faço a importação
    #dentro da função linha 
    from time import sleep

    """
    - Função sem parâmetros
    - Imprime um linha personalizada com um efeito de loading...
    """

    line = '|' * 30

    for i in line:
       # sleep(0.2)
        print(f'{i}', end = '', flush = True)
    print()
    
linha()
print(linha.__doc__)

#argumentos opcionais / funções com return 

#para indicar que os parâmetros são opcionais, eu preciso deixar eles 'valendo alguma coisa por padrão'
# no exemplos abaixo, todos os parâmetros são opcionais, note que todos eles por padrão, valem '0'  
def soma(a = 0, b = 0, c = 0):
    # somando de todos os parâmetros e armazenando o resultado em 's'
    s = a + b + c
    # retornando o valor de 's'
    return s

#provando que os parâmetros são opcionais... 
print(f'O resultado da soma é {soma(4,2,1)}')
print(f'O resultado da soma é {soma(4,2)}')
print(f'O resultado da soma é {soma(4)}')
#explicitando valores
#não precisa ser em ordem 
print(f'O resultado da soma é {soma(c = 5, a = 7, b = 1)}')

#escopo de variáveis 

#esse 'x' fora da função é considerada um variável global
x = 10
def exemplo01():
    #mas esse 'x' dentro da função 'exemplo' é considerada um variável local, ou seja, só pode ser acessada 
    #dentro do escopo da função 'exemplo'
    x = 5
    return x

print(f'x no programa principal vale {x}')
print(f'x no escopo local vale {exemplo01()}')

linha()

#agora se eu quiser modificar a variável 'x' global dentro de uma função, eu preciso utilizar uma palavra 
#reservada chamada global 

def exemplo02():
    #aqui eu uso a palavra reservada 'global' para indicar que eu quero utilizar a variável 'x' do programa 
    #principal
    global x 
    #atribuo 50 ao x global e depois retorno o valor de x
    x = 50
    return x

print(f'x no programa principal vale {x}')
print(f'x global agora vale {exemplo02()}')
