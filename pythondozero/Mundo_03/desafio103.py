# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


#criando a função ficha que recebe 2 parâmetro opcionais, o nome do jogador e o número de gols
def ficha(jogador = "<desconhecido>", gols = 0):
    #retorna o nome do jogador e a quantidade de gols que ele fez  
    return f"O jogador '{jogador}' fez '{gols}' gol(s) no campeonato."

#pede o nome do jogador, converte pra str e deixa a primeira letra de cada palavra em maiúscula
jogador = str(input('Jogador: ')).title()
#pede a quantidade gols e converte pra str (eu preciso converter pra str porque se o usuário não digitar nada
# em 'gols' eu não vou ter problemas porque gols vai ser considerado como uma string vazia)
gols = str(input('Gols: '))

#essas verificações podem ser feitas dentro da própria função 'ficha'
#verifica se gols é númerico
if (gols.isnumeric()):
        #se for, converto gols pra int 
        gols = int(gols)
else:
    #senão, gols recebe 0
    gols = 0

#verifica se jogador é uma string vazia 
if (jogador == ''):
    #se for, eu chamo a função passando como parâmetro apenas os gols 
    print(ficha(gols=gols))
else:
    #senão, passo os dois parâmetros
    print(ficha(jogador, gols))