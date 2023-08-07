#faça um programa que mostre a tabuada de vários números, um de cada vez, para cada 
#valor digitador pelo usuário. o programa será interrompido
#quando o número solicitador for negativo
#enquanto verdade 
while True:
    #pe um número, converte pra int e armazena em n 
    n = int(input('Quer ver a tabuada de qual de qual valor ? '))
    #se o número digitado for menor que 0 o programa mostra uma mensagem e usa o break para encerrar 
    if n < 0:
        print('Programa tabuada encerrado. Volte sempre!')
        break
    #crio um for que vai iniciar no número 1 e vai terminar no 10
    for i in range(1, 11):
        #vai mostrar n, mostra o indice e por fim, o resultado de n x o indice 
        print(f'{n} x {i} = {n*i}')
    
    