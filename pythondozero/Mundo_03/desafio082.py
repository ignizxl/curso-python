# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores 
# pares e  os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


#crio uma lista chamada numeros que inicia vazia 
numeros = []
#crio uma lista chamada pares que inicia vazia 
pares = []
#crio uma lista chamada impares que inicia vazia 
impares = []

#enquanto verdade, faça
while True:
    #pede um valor, converte pra int e armazena em n 
    n = int(input('Digite um número: '))

    #depois uso o append() para adicionar o que foi armazenado em n na lista numeros
    numeros.append(n)

    #faz a verifição se o resto da divisão de n por 2 é igual a 0, se for, n é par.
    if n % 2 == 0:
        #se n for, eu adiciono n na lista pares 
        pares.append(n)
     #senão   
    else:
        #eu adiciono n na lista impares 
        impares.append(n)
    
    #crio um variável chamada continuar que inicia como uma string vazia 
    continuar = ' '
    #flag. enquanto continuar não estiver em SN, faça
    while continuar not in 'SN':
        #pede uma entrada de dado, o input converte pra str por padrão, elimina os espaços
        #com o strip, joga a letra para maiúscula e considera só a primeira letra 
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    #faço a verificação, se continuar for igual a 'N'
    if continuar == 'N':
        #uso o break para interromper o laço while 
        break
#mostro na tela todos os números digitados, todos os números pares digitados e todos os números impares digitados
print(f'A lista completa é {numeros}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')