#importo a funcionalidade factorial para calcular o fatorial do número digitado
from math import factorial
#pede um número inteiro qualquer e armazena em n 
print(' =-= importando biblioteca math.factorial =-= ')
n = int(input('Digite um número: '))
#calcula o fatorial de n utilizando a funcionalidade factorial da biblioteca math e armazena em result
result = factorial(n)
#mostro resultado na tela 
print('{}! = {}'.format(n, result))

print('')

##segunda forma de fazer 

#pede uma entrada de dado, converte para int e armazena em n
print('=-= fatorial usando laço de repetição while =-= ')
n = int(input('Digite um número: '))

#crio um contador chamado c que vai começar valendo n 
c = n
#crio outro contador chamado f que vai valer 1 
f = 1 
#agora vou mostrar na tela o uma mensagem dizendo que vou calcular o fatorial do número digitado, e depois
#uso o end='' para continuar na mesma linha
print('Calculando o fatorial de {}! = '.format(n), end='')
#agora crio um laço while, enquanto o meu c for maior que zero, faça..
while(c > 0):
    #mostro na tela o valor atual de c e continuo na mesma linha
    print('{}'.format(c), end='')
    #agora eu crio duas condições, se o valor de c for maior do que 1, eu escrevo x na tela, senão eu escrevo o sinal  '='
    #e continuo na mesma linha
    print(' x ' if c > 1  else ' = ', end='')

    #agora eu multiplico o f(que vale 1) vezes o c 
    f = f * c 
    #e a cada iteração, o c = c - 1, ou seja, a cada iteração eu tiro 1 
    c = c - 1 
#agora eu mostro o resultado na tela 
print('{}'.format(f))

print('')

#fazendo com o laço for
print('=-= fatorial usando laço de repetição for =-=')
#pede uma entrada de dado, converte para int e armazena em n 
n = int(input('digite um número: '))

#crio um contador chamado j que vai ser multiplicado pelo indice i do laço for, o número 1 é o elemento 
#neutro da multiplicação, por isso que j vale 1
j = 1

#agora vou mostra na tela o número que eu vou calcular o fatorial, e continuo na mesma linha
print('{}! = '.format(n), end='')
#crio um laço de repetição que inicia no número digitado e termina no 1, o ultimo elemento é ignorado, e vou voltando de 1 em 1 a cada iteração

for i in range(n, 0, -1):
    #agora o j vai receber ele mesmo vezes o valor do meu indice i, que diferentemente do while, no for
    # ele já vai diminuindo a cada iteração, por isso que eu não criei outro acumulador  
    j = j * i 
    #pra saida ficar bonita, a cada iteração eu vou testar essas condições, se o meu indice for maior que
    #1, eu continuo na mesma com o x
    if i > 1:
        print('{} x '.format(i), end='')
    #senão, eu continuo na mesma linha com o sinal =
    else:
        print('{} = '.format(i), end='')

#agora eu mostro na tela o resultado final
print('{}'.format(j))
