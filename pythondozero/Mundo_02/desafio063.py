#mostro sinais de - na tela para melhorar a aparência do programa, não é importante!
print('-' * 25)
print('Sequência de fibonacci')
print('-' * 25)

#pede uma entrada de dado, converte pra int e armazena em n
n = int(input('Quantos números você quer mostrar? '))
#o primeiro termo inicia valendo 0 e o segundo valendo 1 
#na sequência de fibonacci a soma dos dois primeiros termos resultado num terceiro termo
termo1 = 0
termo2 = 1
#vou criar um contador que vai iniciar valendo 3, porque eu já vou ter mostrado os 3 primeiros termos, por isso 
#ele inicia valendo 3 
contador = 3

#mostro o primeiro e segundo termo e continuo na mesma linha 
print(' {} -> {}'.format(termo1, termo2), end='')

#crio um laço while. enquanto o meu contador for menor ou igual a n(número de termos que vai ser mostrado)
#faça...
while(contador <= n):
    #o terceiro termo vai ser a soma do termo1 + o termo2 
    termo3 = termo1 + termo2
    #mostro o resultado do terceiro termo e continuo na mesma linha..
    print(' -> {}'.format(termo3), end='')
    
    #agora eu preciso atualizar o primeiro e segundo termo, pra isso eu faço..
    #o primeiro termo vai receber o segundo 
    termo1 = termo2
    #e o segundo termo vai receber o terceiro
    termo2 = termo3
    #e esse processo se repete a cada iteração e os termos sempre vão sendo atualizados
    #e por fim, incremento o contador 
    contador += 1
#no final do laço eu mostro a mensagem fim
print(' -> FIM')