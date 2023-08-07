#crie um programa que vai ler vários números e colocar em uma lista
#depois disso, mostre:
#a-) quantos números foram digitados 
#b-) a lista de valores, ordenada de forma decrescente
#c-)se o valor 5 foi digitado e está ou não na lista


#crio uma lista chamada números que incia vazia 
numeros = []
#crio um contador chamado vezes que inicia valendo 0 e vai sendo incrementado a cada iteração do while 
vezes = 0
#enquanto verdade, faça
while True:
    #pede um valor, converte pra int e armazena em n 
    n = int(input('Digite um valor: '))
    #depois, uso o append pra adicionar o que foi armazenado em n na lista numeros 
    numeros.append(n)
    #e incremento o contador vezes 
    vezes += 1
    #crio um variável chamada continuar que inicia como uma string vazia 
    continuar = ' '
    #crio o meu flag(condição de para do while)
    #enquanto continuar não estiver em SN, isso é, enquanto o usuário não digitar S ou N, o while repete 
    while continuar not in 'SN':
        #pede uma resposta S ou N, elimina os espaços com o strip, joga a letra pra maiúscula e pega só a primeira letra 
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]

    #fora do laço faz a verificação, se continuar for igual N, uso o break para interromper o laço while
    if continuar == 'N':
        break

#ao fim do laço, uso a função sort passando o parâmetro reverse=true para ordenar tudo que está dentro da lista de forma decrescente
numeros.sort(reverse=True)
#mostra a quantidade de números que o usuário digitou 
print(f'Você digitou {vezes} elemenos')
#mostra na tela os numeros armazenados na lista ordenados de forma decrescente 
print(f'Os valores em ordem decrescente são:',end=' ')
print(numeros)

#e por fim, verifica se o número 5 existe dentro da lista
if 5 in numeros:
    #se existir, o valor faz parte 
    print('O valor 5 faz parte da lista!')
#senão, o valor 5 não foi encontrado
else:
    print('O valor 5 não foi encontrado!')

    