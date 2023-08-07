#faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


#vou colocar um acumulador 'primo' para contar quantas vezes o número digitado foi divisivel
#em resumo, se o número digitado foi divisivel apenas 2 vezes, ele é primo, caso contrário, ele não é primo!
primo = 0

#vou começar pedindo um número ao usuário e armazenado o resultado em 'num'
num = int(input('Digite um número: '))

# o meu laço de repetição vai começar no 1 e vai até o número que foi armazenado na variável 'num' + 1. 
# o +1 é usado porque o ultimo número é ignorado
for i in range(1, num+1):

    #se o resto divisão do número digitado por i for igual a zero. faça...
    if num % i == 0:
        # o acumulador 'primo' vai rebecer 'primo'(0) + 1
        # esse acumulador vai contar quantas vezes o número digitado foi divisivel 
        primo = primo + 1
#se o número digitado foi divisivel apenas 2 vezes. faça
if primo == 2:
    #mostre na tela que o número digitado é primo. para o número ser primo ele só pode ser divisivel por 1 e por ele mesmo(número digitado)
    print('O número {} foi divísivel apenas {} vezes.\n por isso ele é PRIMO'.format(num, primo))

#se o número digitado foi divisivel mais de duas vezes, vai entrar nesse else. se entrou nesse else, faça
else:
    #imprima na tela que o número digitado não é primo porque ele foi divisivel mais de 2 vezes 
    print('O número {} foi divísivel {} vezes.\n por isso ele  NÃO é PRIMO'.format(num, primo))
        
