#desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC 
# e mostree seu status, de acordo com a tabela abaixo:
# - abaixo de 18.5: abaixo do peso
# - entre 18.5 e 25: peso ideal 
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida#

#vou começar pedindo o peso do usuário e armazenando o resultado em 'kg'
kg = float(input('Digite o seu peso em kg: '))

#agora vou pedir a altura do usuário e armazenar o resultado em 'altura'
altura = float(input('Digite a sua altura em metros: '))

#para calcular o imc é bem simples, basta dividir o peso pela altura ao quadrado. veja abaixo:
# imc = kg / altura ** 2
imc = kg / (altura ** 2)

#agora vou mostrar na tela o imc do usuário
print('Seu IMC é de {:.2f}'.format(imc))

#se o imc for menor que 18.5 mostre 'abaixo do peso'
if imc < 18.5:
    print('Abaixo do peso')

#se o imc estiver entre 18.5 e 25 mostre 'peso ideal'
elif  imc < 25:
    print('Peso ideal')

#se o imc estiver entre 25 e 30 mostre 'sobrepeso'
elif  imc < 30:
    print('Sobrepeso')

#se o imc estiver entre  30 e 40 mostre 'obesidade' 
elif  imc < 40:
    print('Obesidade')

#se não atender nenhuma das condições acima, significa que o imc é maior que 40, se é maior que 40 mostre 'obesidade mórbida'
else:
    print('Obesidade mórbida')


#posso fazer assim támbem:
#  
#if imc < 18.5:
#    print('Abaixo do peso')
#elif  18.5 <= imc < 25:
#    print('Peso ideal')
#elif  25 <= imc < 30:
#    print('Sobrepeso') 
#elif 30 <= imc < 40:
#    print('Obesidade')
#else:
#    print('Obesidade mórbida')

