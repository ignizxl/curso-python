#comente os seus códigos para facilizar na legibilidade, isso vai facilitar o seu aprendizado!



#calcula média com base em duas notas

#pergunta ao usuário quais foram as suas 1ª e 2ª nota
#como estamos trabalhando com números decimais é necessário fazer a conversão para float 

primeiranota = float(input('Digite a primeira nota: \n'))
segundanota = float(input('Digite a segunda nota: '))

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