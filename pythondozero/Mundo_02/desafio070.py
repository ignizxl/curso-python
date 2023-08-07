#crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. no final, mostre:
#a) qual é o total gasto na compra
#b) quantos produtos custaram mais de R$1000
#c) qual é o nome do produto mais barato 


print('{:=^30}'.format('Carreour'))
#crio vários acumulador, todos iniciam valendo 0
#o acumulador soma total vai ser incrementado cada vez que um preço for lido
soma_total = 0
#a cada iteração, o meu acumulador total de produtos vai ser incrementado
total_de_produtos = 0
#o acumulador mais barato vai acumular o menor preço que foi lido e o nome mais barato vai receber o nome do produto lido  
mais_barato = 0
nome_barato = 0
#toda vez que um preço acima de mil for lido, esse acumulador vai ser incrementado
acima_de_mil = 0

#enquanto verdade faça..
while True:
    #pede o nome de um produto e elimina os espaços com o strip
    produto = str(input('Nome do produto: ')).strip()
    #pede o preço do produto e converte para float 
    preco = float(input('Preço: R$ '))
    #incremente contador total de produtos 
    total_de_produtos += 1
    # o contador soma total vai receber soma total + o preço que foi lido 
    soma_total += preco 
     #se o preço lido for maior ou igual a 1000, faça.
    if preco > 1000:
        #incremente o contador acima de mil 
        acima_de_mil += 1
    #se o total de produtos for igual a 1, significa que é a primeira iteração. faça
    
    #eu poderia fazer dessa forma também

    # if total_de_produtos == 1 or preco < mais_barato:
    #     #esse if vai acontecer se total de produtos for igual a 1 ou se o preço lido for menor que o mais barato
    #     #mais barado recebe o primeiro preço que foi lido 
    #     mais_barato = preco
    #     #nome barato recebe o primeiro nome que foi lido 
    #     nome_barato = produto

    if total_de_produtos == 1:
        #esse if só vai ser atendido na primeira iteração, depois ele vai ser ignorado 
        #mais barado recebe o primeiro preço que foi lido 
        mais_barato = preco
        #nome barato recebe o primeiro nome que foi lido 
        nome_barato = produto

    #se o preço lido for menor que o preço armazenado em mais barato, faça
    if preco < mais_barato:
        #mais barato recebe o preço que foi lido e o nome barato recebe o nome do produto que foi lido
        mais_barato = preco
        nome_barato = produto

   
    
    
    #continuar recebe um string vazia
    continuar = ' '
    #enquanto continuar não estiver em SN. faça
    while continuar not in 'SN':
        #pergunta se o usuário quer continuar, elimina os espaços com o strip, joga a letra para maiúscula e pega a primeira letra
        #e armazena tudo isso em continuar, enquanto o usuário não digitar s ou n, o programa fica perguntando 
        continuar = str(input('Quer continuar comprando? [S/N]')).strip().upper()[0]
    #se continuar estiver em n, ou seja, se o usuário digitar 'n', o break interrompe o laço 
    if continuar in 'N':
        break

#agora é só mostrar na tela a quantidade de produtos e a soma total 
print(f'Você comprou {total_de_produtos} produtos. O total a pagar: R${soma_total:.2f}')
#quantos produtos custaram mais de mil
print(f'Temos {acima_de_mil} produtos que custaram mais de R$1000.00 ')
#e por fim, o nome e o preço do produto mais barato 
print(f'O {nome_barato} foi o produto mais barato, custando apenas {mais_barato:.2f}')
print('{:=^30}'.format('FIM DO PROGRAMA'))