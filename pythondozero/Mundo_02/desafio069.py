#crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
#continuar, no final mostre:
# a - quantas pessoas teme mais de 18 anos
# b - quantos homens foram cadastrados 
# c - quantas mulheres tem menos de 20 anos 

#crio vários acumuladores que vão sendo incrementados se eles atenderem algumas condições 
#idade acima de 18, incremente contador adulto
adultos = 0
#sexo M, incremente contador homens 
homens = 0
#sexo F e idade menor que 20, incremente contador mulheres
mulheres = 0
while True:
    print('-=' * 15)
    print('Cadastre uma pessoa')
    print('-=' * 15) 
    idade = int(input('Idade: '))

    #crio uma string vazia 
    sexo = ' '
    #enquanto não tiver M ou F dentro de sexo, faça
    while sexo not in 'MF':
        #pergunta o sexo, transforma pra letra maiúscula, elimina os espaços e considera apenas a primeira letra
        sexo = input('Sexo: [F/M] ').upper().strip()[0]

    print('-=' * 15)
    #idade acima de 18, incremente contador adulto
    if idade >= 18:
        adultos += 1
    #sexo F e idade menor que 20, incremente contador mulheres
    if idade < 20 and sexo == 'F':
        mulheres += 1
    #sexo F e idade menor que 20, incremente contador mulheres
    if sexo == 'M':
        homens += 1 
    
    #crio uma string vazia 
    continuando = ' '
    #enquanto continuando não tiver SN, faça
    while continuando not in 'SN':
        #pergunta se o usuário quer continuar, joga a letra pra maiúscula elimina os espaço e considera só a primeira letra 
        continuando = input('Quer continuar ? [S/N]: ').upper().strip()[0]
    #se a resposta for diferente de s, o programa encerra 
    if continuando != 'S':
        break
#ao final do laço mostro o que foi acumulado      
print(f'Total de pessoas com mais de 18 anos: {adultos}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} com menos de 20 anos')

