#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, 
#se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo
# do alistamento. seu programa também deverá mostra o tempo que falta ou que passou do prazo.


#vou começar importando a funcionalidade 'date' da biblioteca 'datetime' par pegar o ano atual da máquina
from datetime import date

#agora vou criar uma variável 'anoatual' e vou atribuir o 'date.today().year' que é o ano atual da máquina
anoatual = date.today().year

#vou pedir o sexo do usuário. para isso eu vou explicitar que estou trabalhando com uma string 
#(por isso converto o input para string. por padrão o input já faz essa conversão por isso que não é obrigatório) e depois eu 
#jogo a letra para maiúscula usando o upper () e já elimino os espaços da direita e da esquerda com o strip()
sexo = str(input('Digite seu sexo: \n [M] masculino \n [F] feminino \n Sua opção:')).upper().strip()

#se dentro de sexo tiver a letra m ou a palavra masculino 'M MASCULINO' escreva 'seu alistamento é obrigatório' e o usuário continua o programa 
if sexo in 'M MASCULINO':
    print('O seu alistamento é obrigatório!')

#se o sexo não for masculino, só pode ser feminino. se for feminino escreva 'seu alistamento não é obrigatório' e depois saia do programa
#o quit() vai fazer com que o programa pare de funcionar. se o sexo for feminino o programa para por aqui e não continua, se for masculino 
# o programa continua.
else:
    print('O seu alistamento não é obrigatório!')
    quit()


#agora vou pedir ao usuário qual é o seu ano de nascimento e armazenar o resultado em 'nascimento'
nascimento = int(input('Digite o seu ano de nascimento: '))


#para calcular a idade, basta subtrair o ano atual pelo ano de nascimento.
#para isso vamos fazer: 
#anoatual = date.today().year >>> estou atribuindo o ano atual à variável 'anoatual', e depois é só realizar os calculos normalmente.
# idade = anoatual - nascimento 
#ou eu uso o apenas o date.today().year dessa forma:
# idade = date.today().year - nascimento 
#date.today().year >>> é uma funcionalidade da biblioteca 'datetime' que pega o ano atual da máquina

idade = anoatual - nascimento

#vou mostrar na tela o ano de nascimento que o usuário digitou e quantos anos ele tem no ano atual.
print('Quem nasceu no ano de {} tem {} anos em {}.'.format(nascimento, idade, anoatual))

#se a idade for menor que 18.
#vamos calcular quantos anos faltam para o usuário se alistar
#e para isso, vamos fazer: 18 - idade e para salvar o resultado vamos criar a variável 'faltam'
#faltam = 18 - idade >>> o que sobrar dessa subtração vai ser a quantidade de anos que faltam para o alistamento.

#e depois vamos calcular em que ano será o alistamento do usuário, e para isso vamos fazer.
# sera = faltam + anoatual >>> o resultado da soma da variável 'faltam' + anoatual (date.today().year)
# vai resultar no ano que o usuário deverá fazer o seu alistamento, ou seja, quando o usuário completar os seus 18 anos 
# 
if idade < 18:
    faltam = 18 - idade
    sera = faltam + anoatual
    print('Ainda faltam {} anos para o alistamento'.format(faltam))
    print('Seu alistamento será em {}'.format(sera))


#se a idade for maior que 18.
# vamos calcular quantos anos o usuário passou do prazo, que é 18 anos
# para isso vamos fazer: idade - 18, e para salvar o resultado vamos criar a variável 'passou'
# passou = idade - 18 >>> o resultado dessa subtração vai ser a quantidade de anos que o usuário ultrapassou quando
# completou 18 anos. 
# e depois vamos calcular o ano em que o usuário deveria ter feito o seu alistamento
# para isso vamos fazer: ano atual - passou e para salvar o resultado vamos criar a variável 'foi' 
# foi = anoatual - passou >>> o resultado dessa subtração vai ser o ano em que o usuário deveria  ter feito a seu alistamento.
elif idade > 18:
    passou = idade - 18
    foi = anoatual - passou 
    print('Já deveria ter se alistado há {} anos'.format(passou))
    print('Seu alistamento foi em {}'.format(foi))

#e por fim, vamos usar o else.
#se não é maior e nem menor que 18, só pode ser igual a 18. então por isso que eu vou usar o else.
#se a idade for igual a 18 escreva você tem que se alistar imediatamente 
else:
    print('Você tem que se alistar IMEDIATAMENTE! ')