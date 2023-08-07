#crio um acumulador chamado fim que inicia valendo 1 
fim = 1
#mostro essas mensagens na tela para melhorar a aparência do programa
print('Gerador de pa')
print('=-='*5)
#pede uma entrada de dado, converte para int e armazena em ptermo
ptermo = int(input('Digite o primeiro termo: '))
#pede uma entrada de dado, converte para int e armazena em razao
razao = int(input('Digite a razão da PA: '))
#cria um variável chamada pa e armazena o que foi armazenado em ptermo
pa = ptermo
#enquanto fim for diferente de 10+1, faça..
while(fim != 10+1):
    #mostre o valor de pa(o valor inicial) e continuo na mesma linha usando o end
    print(pa ,end=' -> ')
    #depois que mostrar na tela pa recebe pa mais a razao
    pa += razao
    #e a cada iteração eu incremento o acumulador fim, para quando chegar em 10 o while parar 
    fim += 1
#quando o laço terminar, eu mostro a mensagem FIM 
print('FIM')


#outra forma de fazer.
#pede uma entrada de dado, converte pra int e armazena em primeiro
primeiro = int(input('Digite o primeiro termo: '))
#pede uma entrada de dado, converte pra int e armazena em razao
razao = int(input('Digite a razao da PA: '))
#crio um acumulador que inicia valendo o que foi armazenado em primeiro
termo = primeiro
#crio um contador que inicia valendo 1 e vai sendo incrementado a cada iteração do while
cont = 1
#enquanto o cont for menor ou igual a 10, faça
while(cont <= 10):
    #mostre na tela o acumulador termo e continue na mesma linha
    print('{} -> '.format(termo), end='')
    #o termo recebe termo + a razao
    termo += razao
    #incremente cont + 1 
    cont += 1 
    #e esse processo se repete a cada iteração do while
#no fim do laço, mostre FIM
print('FIM')