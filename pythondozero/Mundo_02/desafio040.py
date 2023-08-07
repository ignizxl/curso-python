#crie um programa que leia duas notas de um aluno e calcule sue média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# média abaixo de 4.0: reprovado
# média entre 4.0 e 6.9: recuperação 
# média 7.0 ou superior: aprovado

#pergunta ao usuário quais foram as suas 1ª e 2ª nota

primeiranota = float(input('Digite a primeira nota: \n'))
segundanota = float(input('Digite a segunda nota: '))

#soma o que foi armazenado nas variavéis (1ª e 2ª nota) e divide por 2
media = (primeiranota + segundanota) / 2 

#escreve na tela a sua 1ª e 2ª nota e mostra qual foi a sua média 
print(f' sua 1ª nota {primeiranota:.1f}, 2ª nota {segundanota:.1f}. A sua media é {media:.1f}')
#print(' sua 1ª nota {:.1f}, 2ª nota {:.1f}.  sua media é {:.1f}'.format(primeiranota, segundanota, media))

#se a média é maior que 7, escreva na tela 'aprovado'
if media >= 7:
    print('O aluno está APROVADO!' )

#se a média está entre 4 e 6, escreva na tela 'recuperação'
#e também vamos calcular quanto será necessário para o aluno ser aprovado
# para isso vamos subtrair 7 que é a média necessária para ser aprovado menos a média do aluno.
# vai ficar assim: necessario = 7 - media 
# elif media >= 4 and media < 7:
# 7 > media >= 4:
elif 4< media <7:
    necessario = 7 - media 
    print('O aluno está em RECUPERAÇÃO! ')
    print('Você precisa de uma nota {} ou superior para ser APROVADO!'.format(necessario))

#se não atendeu nenhuma das condições acima, escreva na tela 'reprovado'
else:
    print('O aluno está REPROVADO! ')