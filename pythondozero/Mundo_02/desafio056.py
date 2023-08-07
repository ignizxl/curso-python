#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
#> a média de idade do grupo
#> qual é o nome do homem mais velho 
#> quantas mulheres têm menos de 20 anos


media = 0
maisvelho = 0
nomemaisvelho = ''
menosde20 = 0


for contador in range(1, 5):
    print('-'*12, f'{contador} ªPessoa', '-'* 12 )
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Qual o seu sexo [M/F] :')).upper()
    media += idade
    
    if idade < 20 and sexo == 'F':
        menosde20 += 1

    if sexo == 'M':
       maisvelho = idade
       nomemaisvelho = nome
    
    elif sexo == 'M' and maisvelho < idade:
        maisvelho = idade 
        nomemaisvelho = nome


    
media = media / 4    
        
                  
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e o seu nome é {}'.format(maisvelho, nomemaisvelho))
print('A quatidade de mulheres com menos de 20 anos de idade é igual a {}'.format(menosde20))