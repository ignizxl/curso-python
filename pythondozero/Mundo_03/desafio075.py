#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#a-) quantas vezes apareceu o valor 9
#b-) em qual posição foi digitado o primeiro valor 3
#c-) quais foram os números pares armazenados dentro da tupla


#ler 4 valores pelo teclado, converte pra int e armazena na tupla numeros
numeros = (  int(input('Digite um número: ')),
             int(input('Digite outro número: ')),
             int(input('Digite mais um número: ')),
             int(input('Digite o último número: '))
            )

#mostra quais foram os 4 valores armazenado dentro da tupla 
print(f'Você digitou os números: {numeros}')
#usa a função count(9) na tupla numeros para ver quantas vezes o número 9 foi digitado
print(f'O número 9 apaceceu {numeros.count(9)} vezes')
#se o número 3 foi armazenado dentro da tupla numeros, faça..
if 3 in numeros:
    #mostre na tela em qual posição o número 3 apareceu utilizando a função index,
    # e depois somo +1 porque a contagem inicia no 0. vai mostra a primeira ocorrência
    print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição')
#senão, mostre a mensagem dizendo que o valor 3 não foi digitado
else:
    print('O valor 3 não foi digitado')
#mostre uma mensagem na tela e continue na mesma linha
print(f'Os valores pares digitados foram: ', end="")
#inicio um contador chamado pares que começa valendo 0
pares = 0
#uso laço for para imprimir na tela, vai repetir 4 vezes porque foram 4 valores armazenados na tupla numeros
#para cada num dentro da tupla numeres, faça
for num in numeros:
    #se o resto da divisão de num por 2 for igual a zero, faça
    if num %  2 == 0:
        #mostre o número e continue na mesma linha
        print(num , end=' ')
        #incremente contador par 
        pares += 1
#se o meu contador pares for igual a 0 significa que não foi digitado nenhum valor par
#então, se ao final do laço o contador pares for igual a 0, faça
if pares == 0:
    #mostre a mensagem 'nenhum'
    print('Nenhum')