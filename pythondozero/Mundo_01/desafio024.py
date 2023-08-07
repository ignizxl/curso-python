#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

#pede pra o usuário digitar o nome de uma cidade e elimina os espaços da direita e da esquerda com o strip e depois
#armazena o que o usuário digitar em 'cidade'
cidade = str(input('Digite o nome de uma cidade: ')).strip()

#agora eu jogo o que foi armazenado em 'cidade' para letra maiúscula
cidade = cidade.upper()

#aqui eu pego tudo que está armazenado em cidade e jogo dentro de uma lista usando o split
cidade = cidade.split()

#e por fim eu pergunto se o primeiro nome da cidade começa com SANTO (o primeiro nome sempre está na posição '0')
#se o primeiro nome começa com 'SANTO' o programa me retorna 'True', caso contrário, o programa retorna 'False'
print('SANTO' in cidade[0])


#segunda forma de resolver esse exercicio
#pede pra o usuário digitar o nome de uma cidade e elimina os espaços da direita e da esquerda com o strip e depois
#armazena o que o usuário digitar em 'cidade'. eu estou convertendo para str para explicitar que é uma string 
cidade = str(input('Digite o nome de uma cidade: ')).strip()

#agora eu pergunto se o nome da cidade começa com 'SANTO'. santo tem 5 letras, então eu faço > 
# ':5' para começar a contagem do '0' e parar a contagem no número 4 (o ultimo número é ignorado)
#depois eu uso o .upper para jogar a letra para maiúsculo e depois comparar se o primeiro nome é igual a 'SANTO'
print(cidade[:5].upper() == 'SANTO')