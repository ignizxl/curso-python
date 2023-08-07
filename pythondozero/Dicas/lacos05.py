#faça um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#posso fazer de várias formas. aqui vão algumas:
#vou começar fazendo um laço de repetição para contar entre o intervalo de 1 a 51 porque o ultimo termo é ignorado, então vai de 1 a 50 
for i in range(1, 51):
#e se o resultado do resto da divisão de i por 2 for igual a 0, ele é par
    if i % 2 == 0:
#mostre os números pares 
        print(i)

#aqui, um laço de repetição para contar entre o intervalo de 2 a 51 pulando de 2 em 2
#a contagem começou do número 2 porque o número 1 vai ser ignorado de toda forma por que ele é impar e aqui eu só quero os pares.
#então começar do números 1 ou do 0, o programa iria fazer algumas repetições que são desnecessárias.
#pra o programa não fazer as repetições desnecessárias, eu já vou iniciar o intervalo entre 2 até 51, porque eu sei que o 0 e o 1 vão ser ignorados
#e se eu começar do 2 até 51 pulando de 2 em 2, o programa já vai direto pegando só os pares e sem fazer repetições que não são 'necessárias' por assim dizer

for i in range(2, 51, 2):
    print(i)
    print('.')


for i in range(2, 51, 2):
    print(i)
    print('.')

#laço de repetição for, inicia a contagem no 1 e termina no 10
for i in range(1, 10+1):
    print(i)
#é bom utilizar o for quando eu sei onde inicia e onde termina 

#laço while 
#crio um contador que inicia valendo zero e vai sendo incrementado a cada iteração 
cont = 0
#enquando o meu contador for menor ou igual a 10 faça
while cont <= 10:
    #mostre o contador
    print(cont)

    #incremente o contador 
    cont += 1 
#quanto o contador chegar em 10 ele para 

#laço while infinito
#crio um contador que inicia valendo zero e vai sendo incrementado a cada iteração 
cont = 0
#o while agora vai ficar repetindo infinitamente, para ele para eu preciso usar o break, que vai fazer com que eu saia do laço
while True:
    print(cont)
#mostro o valor do contador e incremento ele a cada iteração 
    cont +=1 
#se o valor do meu contador for igual a 10, saia do laço
    if cont == 10:
        break

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