# crie um programa que leia vários números inteiros pelo teclado. no final da execução, 
# mostre a média entre todos os valores e qual foi o maior e meor valores lidos.
# o programa deve perguntar ao usuário se ele quer ou não contiuar a digitar valores.

#crio vários acumuladores, todos iniciam valendo 0, exceto o rep. o rep vai ser incrementado quando o usuário digitar n, ai o while para 
soma = 0 #soma todos os número a cada iteração 
divido = 0 #conta o número de vezes que o usuário digitou um número
maior = 0 #vai acumular o maior valor digitado
menor = 0 #vai acumular o menor valor digitado
leitura = 0 #eu inicio esse acumulador valendo 0 pra o acumulador maior e menor iniciar valendo n 
rep = 1
#enquanto rep for diferente de 2, faça...
while (rep != 2):
    #pede pra o usuário digitar um número e converte pra int
    n = int(input('Digite um número: '))
    #se for a primeira leitura do while, faça
    if leitura == 0:
        # maior e menor recebe n
        maior = n
        menor = n
        #senão, faça..
    else:
        #se n for maior, maior recebe n
        if n > maior:
            maior = n
        #se n for menor, menor recebe n 
        if n < menor:
            menor = n
   #incremento o contador leitura e dividido com +1
    leitura += 1 
    divido += 1
    #soma recebe soma + o valor digitado 
    soma += n   
    #pergunta ao usuário se ele quer continuar, s ou n, e joga pra letra maiúscula,
    #  elimino os espaço com o strip e considero apenas a primeira letra
    continuar = input('Quer continuar [S/N]: ').upper().strip()[0]
    #se continuar for igual a n, faça
    if continuar == 'N':
        #incremente o contador rep e o programa encerra
        rep += 1
#calculando a media      
media = soma / divido
#mostra na tela a quantidade de números digitados e a media entre eles
#mostra na tela o maior e menor número digitado
print('Você digitou {} e a média foi de {:.2f}'.format(divido, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


#outra forma

#mais uma vez todos os acumuladores iniciam valendo 0
#resp inicia valendo 'S'
resp = 'S'
soma = 0
media = 0
quantidade = 0
maior = 0
menor = 0
#enquanto o resp estiver em Ss, faça
while(resp in 'Ss'):
    #mesmo esquema da solução anterior 
    num = int(input('Digite um número: '))
    soma += num 
    quantidade += 1

    if quantidade == 1:
        maior = 0
        menor = 0
    else:
        if num > maior:
            maior = num 
        
        if num > menor:
            menor = num
    #pergunta se o usuário quer continuar, se a resposta for sS ele continua(letra maiúscula, elimina espaço e considera só a primeira letra)
    #se for nN o programa para 
    resp = input('Quer continuar? [S/N]').upper().strip()[0]
#calcula a média 
media = soma / quantidade
print('Você digitou {} números e a média entre eles é {:.2f}'.format(quantidade, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))


