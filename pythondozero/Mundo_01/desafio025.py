#crie um programa que liea o nome de uma pessoa e diga se ela tem "SILVA" no nome

#pede o nome do usuário e elimina os espaços indesejados com strip e depois armazena o resultado em 'nome'
#aqui eu estou convertendo para str para explicitar que é uma string 
nome = str(input('Digite o seu nome:')).strip()

#agora eu jogo o que está armazenado em nome para maiúsculo e pergunto 
#se existe "SILVA" dentro de nome. se exite me retorne 'True' e caso contrário vai me retorna 'Falso'
#para isso eu uso o 'in' dessa forma:
#'SILVA' in nome >>> traduzindo: existe silva in nome? existe silva dentro da variável nome ?
print('Seu nome tem SILVA? {}'.format('SILVA' in nome.upper()))