#crio um flag(condição de parada) para fazer o while repetir 
n = 1

#crio dois acumuladores, um chamado cont(vai contar quantos números eu digitei) e outro chamado somatorio
#(vai somar todos os números que forem digitados, exceto 999)
cont = 0
somatorio = 0

#enquanto o meu n for diferente de 999, faça
while n != 999:
    #pede um número inteiro e armazena em n
    n = int(input('Digite um número [999 encerra o programa]: '))

    #pra ignorar a minha condição de parada (999) eu uso o if para verificar se 
    #n é diferente de 999 para incrementar os contadores
    if n != 999:
        #incremente contador cont
        cont += 1 
        #somatorio recebe somatorio + o valor de n 
        somatorio += n

        #e esse processo se repete até que o usuário digite até que o usuário digite 999
        #para encerrar 
#no fim eu mostro quantos números foram digitados e somatório entre eles 
print('Você digitou {} números e a soma entre eles é {}'.format(cont, somatorio))