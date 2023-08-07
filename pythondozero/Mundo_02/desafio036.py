#escreva um programa para aprovar a empréstimo bancário para a compra de uma casa. o programa
# vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o 
# empréstimo será negado#

#vamos perguntar qual é o valor da casa para o usuário e armazenar o resultado em 'valorcs'
valorcs = float(input('Informe o valor da casa: \n R$ '))

#depois vamos pedir o salário do usuário e armazenar o resultado em 'salario'
salario = float(input('Informe o salário do comprador: \n R$ '))
#agora vamos perguntar em quantos anos de financiamento o usuário quer
anos = int(input('Informe quantos anos de financiamento: '))

#para calcular o valor das parcelas primeiro temos que pegar a quantidade de ('anos' e multiplicar por 12)
#(anos * 12) >>> vai ser a quantidade de parcelas.
#e para calcular quanto irá custar cada parcela, vamos pegar o valor da casa e dividir pela quantidade de parcelas
#valorcs / (anos * 12) >>> vai ser quanto irá custar cada parcela
parcelas = valorcs / (anos * 12)

#para calcular os 30% do salário vamos multiplicar o 'salario' por 0.3 ou vamos fazer assim:
# salario * (30/100) >>> é a mesma coisa que multiplicar salario * 0.3
minimo = salario * (30/100)

#agora vou mostrar na tela o valor da casa, quantos anos de financiamento e quanto vai custar cada parcela
print('Para pagar uma casa de R${0:.2f} em {1} anos a prestação será de {2:.2f}'.format(valorcs, anos, parcelas))

#se o valor das parcelas forem menor ou igual os 30% do 'salario' escreva concedido. senão, escreva negado
# o valor das parcelas precisa ser menor ou igual os 30% do salario para o empréstimo ser concedido, se for maior do que os 30%
#o empréstimo será negado

if parcelas <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO')


# print('exceder', minimo)
# print('parcelas',parcelas)
# print('isso aqui é a multiplicação das parcelas x anos x 12',parcelas * anos * 12)