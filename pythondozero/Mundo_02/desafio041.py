#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de uma atleta
# e mostre sua categoria, de acordo com a sua idade:
# - até 9 anos: mirim
# - até 14 anos: infantil
# - até 19 anos: junior
# - até 25 anos: sênior
# - acima: master

#vou começar importando a funcionalidade 'date' da biblioteca 'datetime' par pegar o ano atual da máquina
from datetime import date

#agora vou criar uma variável 'anoatual' e vou atribuir o 'date.today().year' que é o ano atual da máquina
anoatual = date.today().year

#vou pedir o ano de nascimento do usuário e vou armazenar o resultado na variável 'nascimento'
nascimento = int(input('Ano de nascimento: '))

#para calcular a idade, basta subtrair o ano atual pelo ano de nascimento.
#para isso vamos fazer: 
#anoatual = date.today().year >>> estou atribuindo o ano atual à variável 'anoatual', e depois é só realizar os calculos normalmente.
# idade = anoatual - nascimento 
#ou eu uso o apenas o date.today().year dessa forma:
# idade = date.today().year - nascimento 
#date.today().year >>> é uma funcionalidade da biblioteca 'datetime' que pega o ano atual da máquina
idade = anoatual - nascimento

#depois de calcular a idade do usuário, vou mostrar na tela quantos anos ele tem.
print('O atleta tem {} anos.'.format(idade))

#agora vamos para as estrururas condicionais 

# - se a idade for menor que 9 anos: mirim
# - se a idade estiver entre 10 e 14 anos: infantil
# - se a idade estiver entre 15 e 19 anos: junior
# - se a idade estiver entre 20 e 25 anos: sênior
# - se a idade for maior que 25 anos: master

if  idade <= 9:    
    print('Classificação: MIRIM')
elif  idade <= 14:
    print('Classificação: INFANTIL')
elif  idade <= 19:
    print('Classificação: JUNIOR')
elif  idade <= 25:
    print('Classificação: SÊNIOR ')
else:
    print('Classificação: MASTER')



#algumas outras formas de fazer:

#if idade >=1 and  idade <= 9:    
#    print('Classificação: MIRIM')
#elif idade >= 10 and idade <= 14:
#    print('Classificação: INFANTIL')
#elif idade >= 15 and idade <= 19:
#    print('Classificação: JUNIOR')
#elif idade >= 20 and idade <= 25:
#    print('Classificação: SÊNIOR ')
#else:
#    print('Classificação: MASTER')



#if 1 <= idade <= 9:    
#    print('Classificação: MIRIM')
#elif idade <= 14:
#    print('Classificação: INFANTIL')
#elif idade <= 19:
#    print('Classificação: JUNIOR')
#elif idade <= 25:
#    print('Classificação: SÊNIOR ')
#else:
#    print('Classificação: MASTER')
