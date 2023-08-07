#refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


#vou começar pedindo um número ao usuário e depois vou armazenar o resultado em 'n'
n = int(input('Digite um número inteiro para descobrir a sua tabuada: '))
#depois vou criar um laço de repetição de 1 até 10
for i in range(1, 11):
    #e por fim, vou mostrar o resultado final. >>> {o valor de 'n'} x {o valor de 'i'} = {o valor de 'n' vezes 'i'}
    #{:2} >>> isso significa que o valor vai sair com duas casas. rode o programa com o {:2} e depois sem {} e veja a diferença
    #é só para o programa ficar mais organizado
    print('{} x {:2} = {}'.format(n, i, (n * i)))


