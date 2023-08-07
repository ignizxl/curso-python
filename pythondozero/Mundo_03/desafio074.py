#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. depois disso, 
#mostre a listagem de números gerados e também indique o menor e o maior valor estão na tupla.

#da biblioteca random, importe apenas a funcionalidade randint para escolher um número aleatório
from random import randint
#sorteia 5 números aleatórios entre 0 e 9 e armazena, n1 n2 n3 n4  e n5
n1 = randint(0,9)
n2 = randint(0,9)
n3 = randint(0,9)
n4 = randint(0,9)
n5 = randint(0,9)
#joga tudo dentro de uma tupla chamada numeros 
numeros = (n1 , n2, n3, n4, n5)
#mostra os números sorteados na tela 
print(f'Os valores sorteado foram {numeros}')
#usa a função max para pegar o maior valor entre os 5 valores sorteados 
print(f'O maior valor sorteado foi {max(numeros)}')
#usa a função min para pegar o menor valor entre os 5 valores sorteados 
print(f'O menor valor sorteado foi {min(numeros)}')


print()

#outra forma de fazer 
#cria uma tupla chamada numbers e já sorteia todos os 5 números dentro da própria tupla
numbers = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9) )
#mostra uma mensagem na tela e continua na mesma linha 
print('Os números sorteados foram: ', end='')
#para cada num dentro da tupla numbers(x,x,x,x,x), mostre o valor 
#isto é, cria um laço de repetição que vai repetir 5 vezes por que são 5 números que vão ser sorteados, e a 
# cada iteração mostra o 1ª sorteado e continua na mesma linha, 2ª sorteado e continua na mesma linha e por ai vai 
for num in numbers:
    #mostra o número sorteado e continua na mesma linha 
    print(num , end=' ')

#usa a função max para pegar o maior valor entre os 5 valores sorteados, e uso o \n para 'quebrar a linha'
#para não continuar na mesma linha e pular para a próxima
print(f'\nO maior valor sorteado foi: {max(numbers)}')
#usa a função min para pegar o menor valor entre os 5 valores sorteados 
print(f'O menor valor sorteado foi: {min(numbers)}')

