
#pede um valor, converte para int e armazena em n1
n1 = int(input('Primeiro valor:'))
#pede um valor, converte para int e armazena em n2
n2 = int(input('Segundo valor: '))

#atribuo o valor 0 a variável op
op = 0

#enquanto op for diferente de 5, repita
#se o usuário digitar 5 o programa encerra
while (op != 5):
    
    #mostro o menu na tela e suas opções
    print("""
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair do programa """)
#depois peço para o usuário digitar a sua opção entre 1 e 5 e armazeno o resultado em op
    op = int(input('Qual é a sua opção? '))

#se a opção for 1, some os dois valores e mostre na tela
    if op == 1:
        resultado = n1 + n2
        print('----> A soma entre {} e {} é igual a {}'.format(n1, n2, resultado))
#se a opção for 2, multiplique os dois valores e mostre na tela
    elif op == 2:
        resultado = n1 * n2
        print('----> A multiplicação entre {} e {} é igual a {}'.format(n1, n2, resultado))
#se a opção for 3, mostre qual dos dois valores é o maior, ou se menor ou se eles são iguais
# e mostre na tela 
    elif op == 3:
        if n1 > n2:
            maior = n1
            print('----> {} é maior '.format(maior))
        elif n1 == n2:
            print('----> Os números são iguais')
        else:
            menor = n2
            print('----> {} é menor'.format(menor))

#se a opção for 4, peça dois novos valores e armazene o primeiro em n1 e o segundo em n2           
    elif op == 4:
        n1 = int(input('N Primeiro valor:'))
        n2 = int(input('N Segundo valor: '))

    #se o usuário digitar alguma opção que seja diferente de 1,2,3,4 ou 5, mostre na tela opção inválida    
    else:
        print("----> opção inválida, tente novamente!")

