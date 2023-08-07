#desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o.

# vou atribuir 0  a variável soma
soma = 0
# vou atribuir 0 a variável acumulador 
acumulador = 0

# vou criar um laço de repetição de 1 até 6 e vou pedir para o usuário digitar um número e armazenar o resultado em 'num' 
#e esse processo vai se repetir 6 vezes
for i in range(1, 7):
    #pede um número e armazena o resultado em 'num'
    num = int(input('Digite um número: '))
    #se o resto da divisão por 2 do número digitado for zero ele é par 
    if num % 2 == 0:
        #soma vai receber soma(0) + o número par que foi digitado e esse processo se repete
        soma = soma + num
        #acumulador vai receber acumulador(0) + 1 e esse processo se repete 
        #esse processo só vai se repetir se os números digitado forem par!!
        acumulador = acumulador + 1

# e agora vou mostrar na tela a quantidade de números pares digitados e a soma dos números pares digitados
print('Você informou {} números pares e a soma dos pares informados é igual a {}'.format(acumulador, soma)) 