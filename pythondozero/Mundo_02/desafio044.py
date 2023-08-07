#elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto 
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros#

#vou começar imprimindo na tela uma saída formatada para melhorar a aparência do programa
#print('{:=^30}'.format(' Lojas americanas ')) >>> significa que eu vou 'Lojas americanas' em 30 espaços de forma centralizada entre sinais de '='
print('{:=^30}'.format(' Lojas americanas '))

# agora vou pedir um valor ao usuário e vou armazenar o resultado em 'valor'
# como estamos trabalhando com dinheiro precisamos converter o valor digitado no 'input' para 'float' que são valores reais, decimais
valor = float(input('Preço das compras: \n R$ '))


#para não usar o 'print' varias vezes eu uso o 'print' apenas uma vez e escrevo um 'texto comprido' entre as 3 aspas que vai facilitar muito
# forma eficiente e produtiva:
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''') 

#forma menos produtiva
#print('FORMAS DE PAGAMENTO')
#print('[ 1 ] à vista dinheiro/cheque')
#print('[ 2 ] à vista cartão')
#print('[ 3 ] 2x no cartão')
#print('[ 4 ] 3x ou mais no cartão')


#agora eu vou pedir para o usuário escolher uma das 4 opções acima e vou armazenar o resulta acima
# como o usuário vai digitar "1, 2, 3, 4" uma dessas opções que são números inteiros, eu preciso fazer a conversão para 'int' para números inteiros 
op = int(input('Sua opção: '))

#agora vamos para as condições aninhadas

#se a opção escolhida for 1, pegue o valor digitado e calcule 10% de desconto
#nos exercicios anteriores já foi explicado como calcular aumentos e descontos
#para resumir: vou pegar o valor digitado e vou subtrair pelo valor multiplicado por 10 sobre 100 ou por 0.1 que equivale a 10%
#depois armazeno tudo em 'total' 
if op == 1:
    total = valor - (valor * 10/100)

#se a opção escolhida for 2, pegue o valor digitado e calcule 5% de desconto
#o calculo aqui é feito da mesma forma que foi feito na opção 1, só que, vai ser com os 5%
# depois armazeno tudo em 'total' 
elif op == 2:
    total = valor - (valor * 5/100)

#se a opção escolhida for 3, pegue o valor digitado e divida por 2
#vou armazenar o valor digitado em 'total'
#e vou criar a variável 'parcela' e vou pegar o que foi armazenado em 'total' e dividir por 2 
elif op == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))

#se a opção escolhida for 4, calcule 20% de juros do valor
#para essa 4 opção, vou criar um if. se a quantidade de parcelas digitada for maior ou igual a 3.
#calcule os 20% de juros dessa forma.
#vou criar a variável 'total' e vou calcular os 20% de juros pegando o 'valor' digitado e vou multiplicar por 20 sobre 100 e 
#depois vou somar com o 'valor' 
#  
elif op == 4:
#vou pedir a quantidade parcela ao usuário e vou armazenar o resultado em 'parcelas'
    parcelas = int(input('Quantas parcelas: '))
#vou criar um if. se a quantidade de parcelas digitada for maior ou igual a 3, calcule os 20% de juros.
    if parcelas >= 3:
#vou criar a variável 'total' e vou calcular os 20% de juros pegando o 'valor' digitado e vou multiplicar por 20 sobre 100 e 
#depois vou somar com o 'valor' 
#depois vou criar a 'variável valordaparcela' e vou pegar a variável 'total' e vou dividir pela variável 'parcelas'
        total = (valor * 20 / 100) + valor 
        valordeparcela = total / parcelas
#e agora eu vou imprimir uma mensagem na tela que só vai aparecer se a condição do if acima for atendida.
#mostre na tela o valor da compra, a quantidade de parcelas e o valor de cada parcela
        print('Sua compra de R${:.2f} vai ser parcelada em {}x de R${:.2f} com juros'.format(valor, parcelas, valordeparcela))
    
#se a condição do if não foi atentida, vai entrar no else, ou seja, a quantidade de parcelas que o usuário digitou é menor que 3
#e se entrar no else, o usuário vai sair do programa
#quit() >>> significa que vai sair do programa     
    else:
        print('A quantidade de parcelas é menor que 3. Tente novamente')
        quit()

#se o usuário não digitou nenhuma das 4 opções acima mostre na tela, 'OPÇÃO INVÁLIDA de pagamento. Tente novamente'
#criei a variável 'total' e vou armazenar o valor digitado em 'total'
#essa variável 'total' é obrigatória porque eu tenho um print fora das condições que sempre está imprimindo na tela a variável 'valor' e a variável 'total'
#se entra nesse else e eu não colocar essa variável 'total' vai dar um erro na hora de imprimir
else:
    total = valor 
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

#e por fim, sempre vai imprimir esse linha de comando, mostrando o valor digitado e quanto que sua compra vai custar no final.
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))





#a diferença dessa segunda forma é que os 'prints' estão todos dentro de condições, note que não tem nenhum print fora de uma condição.
#ou seja, só vai aparecer alguma coisa na tela se alguma das condições abaixo forem atendidas 

# if op == 1:
#     total = valor - (valor * 10/100)
#     print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))
# elif op == 2:
#     total = valor - (valor * 5/100)
#     print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))
# elif op == 3:
#     total = valor / 2
#     print('Sua compra de R${:.2f} vai custar 2x de R${:.2f} sem juros'.format(valor, total))
# elif op == 4:
#     parcelas = int(input('Quantas parcelas: '))
#     if parcelas >= 3:
#         total = (valor * 20 / 100) + valor 
#         valordeparcela = total / parcelas
#         print('Sua compra de R${:.2f} vai ser parcelada em {}x de R${:.2f} com juros'.format(valor, parcelas, valordeparcela))
#         print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
#     else:
#         print('A quantidade de parcelas é menor que 3')
#         quit()

# else:
#     total = valor
#     print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
#     print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))