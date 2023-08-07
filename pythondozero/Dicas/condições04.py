#vamos ver um pouco sobre as estruturas condicionais em python
#

#calcula média com base em duas notas

#pergunta ao usuário quais foram as suas 1ª e 2ª nota

primeiranota = int(input('Digite a primeira nota: \n'))
segundanota = int(input('Digite a segunda nota: '))

#soma o que foi armazenado nas variavéis (1ª e 2ª nota) e divide por 2
media = (primeiranota + segundanota) / 2 

#escreve na tela a sua 1ª e 2ª nota e mostra qual foi a sua média 
print(f' sua 1ª nota {primeiranota:.1f}, 2ª nota {segundanota:.1f}.  sua media é {media:.1f}')
#print(' sua 1ª nota {:.1f}, 2ª nota {:.1f}.  sua media é {:.1f}'.format(primeiranota, segundanota, media))

#se a média é maior que 7, escreva na tela aprovado
if media >= 7:
    print('aprovado' )

#se a média está entre 4 e 6, escreva na tela final 
elif 4< media <7:
    print('final')

#se não atendeu nenhuma das condições acima, escreva na tela reprovado
else:
    print('reprovado')
#o print abaixo é um comando que sempre vai imprimir na tela por que ele não está identado dentro do else:
#todo comando que está colado no lado esquerdo e sem identação, vai acontecer.
print('Tenha um bom dia!')

#sempre que usar o if, elif e else, depois de dizer as condições, não esqueça de colocar os dois pontos ':' no final da linha e
#também não esqueça de colocar a identação correta usando a tecla tab do seu teclado
#veja o exemplo abaixo:

#if media >= 7:
    #print('aprovado' )

#se a média está entre 4 e 6, escreva na tela final 
#elif 4< media <7:
    #print('final')

#se não atendeu nenhuma das condições acima, escreva na tela reprovado
#else:
#    print('reprovado')

#estruturas condicionais simples não tem o else e nem o elif, tem apenas o if.
#já as estruturas condicionais compostas possui os 3, if, elif e else.






#deselvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem.
#cobrando R$0,50 por cada km para viagens de até 200km e R$0,45 para viagens mais longas.

#vou começar pedindo a distância de da viagem e vou armazenar o resultado em 'km'
km = float(input('Qual é a distância da sua viagem? \n Informe aqui:'))
#vai imprimir na tela uma mensagem dizendo que a mensagem vai começar 
print('Você está prestes a começar uma viagem de {0:.2f} km.'.format(km))

#agora vou calcular o preço da viagem, se 'km' for menor ou igual a 200, eu multiplico 'km' por 0.50. se km for maior que
#200, eu multiplico 'km' por 0.45

#existem duas formas de escrever as condições if e else com o que foi visto até agora. 
#a forma simplificada, que está escrita abaixo. particularmente eu não gosto, mas, funciona do mesmo jeito.
preco = km * 0.50 if km <=200 else km * 0.45
 
#e existe a forma que eu  estou usando com mais frequência nos exercicios.
#forma escrita abaixo:  
#if km <= 200:
#    preco = km * 0.50 
#else:
#    preco = km * 0.45

#depois de calcular preço da passagem, agora vou imprimir na tela quanto que irá custar a passagem da viagem
print('E o preço de sua passagem será de R${0:.2f}'.format(preco))




#condições aninhadas

#if: >>> se 
#elif: >>> senão se 
#else: >>> senão 
#obs: nas condições aninhadas, sempre vai começar com um if, jamais eu posso começar com um elif um else.
#o elif e o else são opcionais.
#dentro de um if eu posso usar quantos 'elif' eu quiser, já o else, eu só posso usar nenhuma ou apenas uma vez!


#nas condições aninhadas o processo é bem semelhante das condições simples e compostas
#veja o exemplo a seguir:

#peço o nome do usuário, jogo a letra para maiúscula, elimino os espaços indejados e armazeno tudo isso em 'nome'
nome = str(input('Qual é o seu nome ?')).upper().strip()

#agora vamos usar as condições aninhadas.
#se o nome for igual a 'igor' escreva 'seu nome é lindo'
if nome == 'IGOR':
    print('Seu nome é lindo!')

#se o nome for 'jake ' ou 'john' escreva 'você tem nome de ator de hollywood'
elif nome == 'JAKE' or 'JOHN':
    print('Você tem nome de ator de hollywood')

#se dentro do nome tiver algun dos nomes ' jason paul khabib' escreva 'seu nome é de campeão'
elif nome in 'JASON PAUL KHABIB':
    print('Seu nome é de campeão')
#se não atender nenhuma das condições acima, escreva 'seu nome é tão normal'
else:
    print('Seu nome é tão normal')

#escreva o nome que o usuário digitou e uma mensagem de bom dia
print('Olá, {0}. Tenha um bom dia'.format(nome)) 