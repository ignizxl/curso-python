#crie um programa que tenha uma tupla única com nomes de produtos e seu respectivos proços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#mostra na tela 40 vezes o sinal de -
print('-' * 40)
#mostra a frase listagem de produtos centralizada em 40 espaços 
print(f'{"LISTAGEM DE PRODUTOS":^40}')
#mostra na tela 40 vezes o sinal de -
print('-' * 40)

#armazena o nome do produto seguido do seu preço dentro da tupla listagem
listagem = ('Lápis' , 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90
            )

#cria um laço de repetição que inicia no zero e vai até o comprimento/tamanho 
#dos elementos existentes dentro da tupla listagem
for item in range(0, len(listagem)):
    #nessa forma de impressão se eu usar o print(item), vai me retorna um número, esse número representa 
    #a posição de um elemento dentro da tupla, e pra imprimir a posição eu faço, listagem[posição]
    #o nome do produto aparece nas posições pares e os preços nas posições impares

    #então, se o resto da divisão de item por 2 for igual a 0, faça
    if item % 2 == 0:
        #dentro de listagem mostre o elemento na posição item, seguido de '.' alinhado 
        # a esquerda em 30 espaços e continua na mesma linha
        print(f'{listagem[item]:.<30}' ,end='')
    #senão, faça
    else:
        #dentro de listagem mostre o elemento na posição item,alinhado a esqueda em 7 espaços com duas 
        #casas flutuantes
        print(f'R${listagem[item]:>7.2f}')
#mostre o sinal de - 40 vezes 
print('-' * 40)