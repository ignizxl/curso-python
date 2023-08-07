#escreva um programa que leia a velicidade de um carro. se ele ultrapassar 80km/h, 
# mostre uma mensagem dizendo que ele foi multado. a multa vai custar R$7,00 por cada km acima do limite.

#vou começar perguntando qual é a velocidade atual do carro para o usuário e vou armazenar o resultado na variável 'vel'
vel = float(input('Digite a velocidade atual do carro: '))
#se a velocidade que o usuário digitou for maior que 80km/h, vai imprimir na tela que ele foi MULTADO por exceder o limite de velocidade
#se excedeu o limite de velocidade vai pagar multa de R$7,00 por cada km ultrapassado
#para calcular a multa é bem simples, primeiro vamos pegar a velocidade atual e subtrair por 80, dessa forma vai sobrar apenas o que foi
#ultrapassado, e depois vamos multiplicar o que foi ultrapassado por 7. vai ficar assim:
# multa = (vel - 80) * 7 
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! você excedeu o limite de velecidade permitido, que é 80km/h. \n Sua multa vai custar: R${:.2f}'.format(multa))
#esse print abaixo sempre vai ser executado, ou seja, não importa se o usuário excedeu ou não excedeu o limite de velocidade, esse print
#sempre será mostrado na tela, ele está colado no lado esquerdo e está sem a identação, por isso que ele vai ser exibido na tela sempre que
#o programa for executado, se ele estivesse dentro do if, ele só iria ser exibido na tela se as condições do if fossem atendidas, 
# nesse exemplo, para as condições do if serem atendidas o usuário precisa exceder o limite de 80km/h.
print('tenha um bom dia, dirija com segurança!')