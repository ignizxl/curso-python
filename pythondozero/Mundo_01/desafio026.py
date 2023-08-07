#faça um programa que leia uma frase pelo teclado e mostre:
#>quantas vezes aparece a letra "A".
#>em  que posição ela aparece a primeira vez.
#>em que posição ela aparece a última vez.

#começo pedindo pra o usuário digitar uma frase e já elimino os espaços indesejados com o strip. depois armazeno o resultado em 'frase'
#obs: converti para str para explicitar que estou trabalhando com string 
#considere que a contagem inicia do 0
frase = str(input('Digite uma frase: \n')).strip()

#agora vou jogar a frase para maiúsculo e vou usar o .count('A') para contar a quantidade de 'A' que aparece na 'frase'
print('A letra "A" aparece {} vezes'.format(frase.upper().count('A')))
#depois vou jogar a frase para maiúsculo de novo e vou usar o .find('A') para mostra em que posição o "A" aparece pela primeira vez.
#find(vai da esquerda para direita) > inicia a contagem da posição 0(primeira caractere) e vai até a posição que a letra "A" aparece pela primeira vez

#ex: n = 'joao santos'
#   print(n.upper().find('A'))
#   o find vai iniciar a contagem do primeiro caractere(posição 0) e vai parar na posição 2 que é onde aparece o primeiro "A" 
print('A primeira vez que a letra "A" aparece é na posição {}'.format(frase.upper().find('A')))

#e por fim vamos jogar a frase mais uma vez para maiúsculo e vamos usar o rfind que vai iniciar a contagem do ultimo caractere, 
# ou seja, vai iniciar a contagem de direita para esquerda. por isso rfind (r de right)
#ex:  n = 'joao santos'
#   print(n.upper().rfind('A'))
#o find inicia a contagem do primeiro caractere ,ou seja, posição 0 (esquerda para direita)
#já o rfind inicia a contagem do ultimo caractere (direita para esquerda)
#então o rfind vai mostra a posição em que a letra "A" aparece pela primeira vez, iniciando a contagem do ultimo caractere até o primeiro.

print('A última vez que a letra "A" aparece é na posição {}'.format(frase.upper().rfind('A')))



#segunda forma de fazer esse exercicio
#aqui eu já jogo a frase para maiúsculo, elimino os espaços e armazeno tudo em 'frase'.
# ao invés de jogar a frase para maiúsculo no .format 
frase = str(input('Digite uma frase: \n')).upper().strip()

#agora vou usar o .count('A') para contar a quantidade de 'A' que aparece na 'frase'
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
# vou usar o .find('A') para mostra em que posição o "A" aparece pela primeira vez.
#find(vai da esquerda para direita) > inicia a contagem da posição 0(primeira caractere) e vai até a posição que a letra "A" aparece pela primeira vez

#ex: n = 'joao santos'
#   print(n.upper().find('A'))
#   o find vai iniciar a contagem do primeiro caractere(posição 0) e vai parar na posição 2 que é onde aparece o primeiro "A" 
print('A primeira vez que a letra "A" aparece é na posição {}'.format(frase.find('A') + 1))

#e por fim  vamos usar o rfind que vai iniciar a contagem do ultimo caractere, 
# ou seja, vai iniciar a contagem de direita para esquerda. por isso rfind (r de right)
#ex:  n = 'joao santos'
#   print(n.upper().rfind('A'))
#o find inicia a contagem do primeiro caractere ,ou seja, posição 0 (esquerda para direita)
#já o rfind inicia a contagem do ultimo caractere (direita para esquerda)
#então o rfind vai mostra a posição em que a letra "A" aparece pela primeira vez, iniciando a contagem do ultimo caractere até o primeiro.

print('A última vez que a letra "A" aparece é na posição {}'.format(frase.rfind('A') + 1))

# explicação do porque do '+1'
#para o python a contagem inicia do 0, e para nós a contagem inicia do 1
#então adicionando o +1 podemos iniciar a contagem dos caracteres da posição 1
#faça o teste digitando 'arara azul' no primeiro programa e depois nesse programa 
