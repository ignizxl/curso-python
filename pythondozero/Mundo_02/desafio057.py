#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#caso esteja errado, peça a digitação novamente até ter um valor correto.

#pede uma entrada de dados do tipo str, elimina os espaços com o strip, 
# joga tudo pra maiúsculo e pega a primeira letra [0] e por fim armazena sexo
sexo = str(input("Informe o seu sexo: [M/F]")).strip().upper()[0]

#se o que foi armazenado em sexo não estiver em 'MmFf', faça
if sexo not in 'MmFf':
    #o while vai ficar repetindo 
    while True:
        #e pedindo mais uma vez entrada de dados do tipo str, elimina os espaços com o strip, 
# joga tudo pra maiúsculo e pega a primeira letra [0] e por fim armazena tudo em tentativa
        tentativa = str(input("Dados inválidos. Por favor, informe seu sexo:")).strip().upper()[0]

        #se a primeira letra que do que foi armzenado em tentativa for igual a 'M' ou 'F', faça
        if tentativa == 'M' or tentativa == 'F':
            # sexo vai receber o que foi armazenado em tentativa e vou usar o break para parar o programa 
            sexo = tentativa
            break
#por fim vou imprimir na tela o sexo que foi escolhido 
print('Sexo {} registrado com sucesso.'.format(sexo))


print('SEGUNDA FORMA:')
#forma mais simples.

#pede uma entrada de dados do tipo str, elimina os espaços com o strip, 
# joga tudo pra maiúsculo e pega a primeira letra [0] e por fim armazena sexo
sexo = str(input("Informe o seu sexo: [M/F]")).strip().upper()[0]

#enquanto sexo não estiver em MmFf
while sexo not in 'MmFf':
    #pede uma entrada de dados do tipo str, elimina os espaços com o strip, 
    # joga tudo pra maiúsculo e pega a primeira letra [0] e por fim armazena sexo.
    #o while vai repetir até que a entrada de dados sexa igual a 'MmFf' uma dessas letras
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo:")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))