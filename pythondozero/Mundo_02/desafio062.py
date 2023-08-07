#pede uma entrada de dado, converte pra int e armazena em primeiro
primeiro = int(input('Digite o primeiro termo: '))
#pede uma entrada de dado, converte pra int e armazena em razao
razao = int(input('Digite a razao da PA: '))
#crio um acumulador que inicia valendo o que foi armazenado em primeiro
termo = primeiro
#crio um contador que inicia valendo 1 e vai sendo incrementado a cada iteração do while
cont = 1
#crio um acumulador chamado total que inicia valendo 0
total = 0 
#crio um acumulador que inicia valendo 10, porque o programa vai mostra os 10 primeiros termos de uma pa
#e depois vai perguntar se o usuário quer mostrar mais alguns novos termos
mais = 10 
#enquanto o que foi acumulado em mais for diferente de 0, faça...
while (mais != 0):
    # total recebe total + o acumulador mais
    total = total + mais
    #enquanto o meu contador for menor ou igual o valor de total, faça...
    while(cont <= total):
        #mostre na tela o acumulador termo e continue na mesma linha
        print('{} -> '.format(termo), end='')
        #o termo recebe termo + a razao
        termo += razao
        #incremente cont + 1 
        cont += 1 
        #e esse processo se repete a cada iteração do while
        #no fim do laço, mostre pausa
    print('PAUSA')
    #ao fim do laço, pergunte quantos termos o usuário quer mostra a mais. se o usuário digitar 
    #0 o programa encerra
    mais = int(input('Quantos termos você quer mostrar a mais? '))
#por fim, mostro o total de termos na tela 
print('Progressão finalizada com {} termos mostrados. '.format(total))

