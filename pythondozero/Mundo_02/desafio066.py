#crie um programa leia vários números inteiros pelo teclado.
#o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
#no final, mostre quantos números foram digitados e qual foi a soma entre eles. #desconsiderando o flag

#crio um acumulador chamado soma que vai iniciar valendo 0 e vai sendo incrementado a cada iteração 
soma = 0
#o acumulador quantidade vai iniciar valendo 0 e vai sendo incrementado a cada iteração
quantidade = 0
#enquanto verdade, faça
while True:
    #pede um número intero, se o número for igual a 999, encerra
    n = int(input('Digite um número: [999 encerra o programa]'))
    #faz a verificação se o número digitado é igual a 999, se for igual a 999 o programa encerra, se não for ele continua 
    if n == 999:
        #break faz sair do laço
        break
    #soma recebe soma + o valor de n 
    soma += n
    #incremente o contador 
    quantidade += 1 
#mostra na tela o resultado final 
print(f'Você digitou {quantidade} números e soma entre eles é {soma}.')