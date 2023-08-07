#faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e o menor peso lidos.


#vou começar criando dois acumuladores


#o maiorpeso começa recebendo o valor '0'
maiorpeso = 0
#e o menorpeso também começa recebendo o valor '0'
menorpeso = 0

#vou criar um laço de repetição for para pedir ao usuário o peso de 5 pessoas 
for contador in range(1, 6):
    #agora vou pedir para o usuário digitar o peso das 5 pessoas e armazenar o resultado na variável 'peso'
    peso = float(input('Digite o peso da {}ªPessoa: '.format(contador)))

#para os acumuludores receberem o primeiro peso que foi digitado eu preciso criar um if
#se o contador for igual a 1,(a primeira iteração, o contador represento o número de iteração) os acumuladores recebem o peso que foi 
#digitado
    if contador == 1:
        maiorpeso = peso
        menorpeso = peso
    
#agora vou criar um else, ele só vai acontecer apartir da segunda iteração até a ultima    
    else:
        #agora vou criar um if, se o peso que foi digitado for maior que o valor acumulado(maiorpeso). faça:
        if peso > maiorpeso:
        #o valor acumulado(maiorpeso) agora vai receber o peso que foi digitado, e até então, esse vai passar a ser o maior peso
            maiorpeso = peso
        #se o peso que foi digitado for menor que o valor acumulado(menorpeso). faça:
        if peso < menorpeso:
        #o valor acumulado(menorpeso) vai receber o peso que foi digitado, e até então, esse vai passar a ser o menor peso
            menorpeso = peso
   

#agora eu mostra na tela o maior e o menor peso que foi lido 
print('O maior peso lido foi {} e o menor peso lido foi {}'.format(maiorpeso, menorpeso))