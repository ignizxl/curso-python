# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

# valor = int(input('Digite quantos R$ você deseja sacar: '))

# while True:
    
#     nota50 = valor // 50
#     valor %=  50
#     nota20 = valor // 20
#     valor %= 20
#     nota10 = valor // 10
#     valor %= 10
#     nota1 = valor // 1

#     if valor == 0:
#         break

# print(f"notas de 50 = {nota50}")
# print(f"notas de 20 = {nota20}")
# print(f"notas de 10 = {nota10}")
# print(f"notas de 1 = {nota1}")

#pede o valor que o usuário quer sacar, converte pra int e armazena em valor
valor = int(input('Quantos R$ você deseja sacar? R$ '))
#total recebe o valor que foi armazenado em valor 
total = valor 
#cedula recebe 50
cedula = 50
#esse acumulador irá contar a quantidade de cedulas como já diz o próprio nome 
quantidade_cedulas = 0
#enquanto verdade, faça
while True:
    #se o total for maior ou igual a minha cedula de 50, faça
    if total >= cedula:
        #eu vou tentar tirar 50 reais do valor digitador a cada iteração, até que não seja mais possível
        total -= cedula
        #e incremento o contador 
        quantidade_cedulas += 1
    
    #senão
    else:
        #mostra a quantidade de cedulas e o valor da cedula 
        print(f'Total de {quantidade_cedulas} cédulas de R${cedula}')
        #verifica se a minha cedula atual é igual a 50, se for, faça
        if cedula == 50:
            #minha cedula atual passa a ser 20
            cedula = 20
        #senão, se a minha cedula atual for igual 20, faça..
        elif cedula == 20:
            #minha cedula atual passa a ser 10
            cedula = 10
        #senão, se a minha cedula atual for igual a 10, faça
        elif cedula == 10:
            #minha cedula atual vai passar a ser 1
            cedula = 1
        
        #e a cada iteração eu zero a quantidade de cedula
        quantidade_cedulas = 0

        #se o meu total for igual a zero, significa que o dinheiro acabou!
        if total == 0:
            break

