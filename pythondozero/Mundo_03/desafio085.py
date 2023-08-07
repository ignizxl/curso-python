# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

#crio uma lista chamada pares e impares e dentro dessa lista eu crio duas 'sublistas' 
pares_e_impares = [[], []]
#crio uma lista chamada número 
numeros = []
#crio um laço de repetição for que vai do 1 até o número 7
for indice in range(1, 7+1):
    #a cada iteração do laço for eu peço pra o usuário digitar um número
    #e já adiciono o número digitado na lista números 
    numeros.append(int(input(f'Digite o {indice}º número: ')))
#agora eu vou cria um laço for para 'varrer' todos os elementos da lista numeros
for indice in numeros:
    #agora vou fazer a verificação se o elemento(indice) é impar ou par 
    #se o resto da divisão do indice por 2 for igual a zero, ele é par
    if indice % 2 == 0:
        #se ele é par, eu vou adicionar o indice na sublista 0 dentro de pares_e_impares
        pares_e_impares[0].append(indice)
    #senão, eu faço
    else:
        #eu vou adicionar o indice na sublista 1 dentro de pares_e_impares
        pares_e_impares[1].append(indice)
#agora eu vou mostrar os valores pares armazenados dentro da sublista 0 dentro de pares e impares
# e uso o metódo sorted para ordenar os elementos de forma crescente 
# e repito o mesmo processo para mostrar os impares 
print(f'Os valores pares digitados foram: {sorted(pares_e_impares[0])}')
print(f'Os valores ímpares digitados foram: {sorted(pares_e_impares[1])}')

print('-' * 20)
#outra forma de fazer
#crio uma lista chamada num com duas sublistas dentro 
#num[0] representa os números pares e num[1] representa os números impares 
num = [[], []]
#crio uma laço for para pedir 7 valores 
for i in range(1, 8):
    #pede um valor, converte pra int e armazena em valor 
    valor = int(input(f'Digite {i}º valor: '))
    #se o resto da divisão de valor por 2 for igual a zero, é par 
    if valor % 2 == 0:
        #se for par, eu uso o metódo append para o valor digitado na lista num[0]
        num[0].append(valor)
    else:
        #senão eu adiciono o valor digitado na lista num[1]
        num[1].append(valor)
print('-=-'*15)
#uso o metódo sort nas sublistas num[0] e num[1] para ordenar os valores armazenados de forma crescente 
num[0].sort()
num[1].sort()
#mostro os valores na tela 
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')