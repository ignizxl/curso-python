#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários superiores a R$1250,00, calcule um aumento de 10%.
#para inferiores ou iguais, o aumento é de 15%.

#pede um valor ao usuário e depois armazena o resultado em 's' 
s = float(input('Informe o salário do funcionário: R$'))


#para calcular o aumento é simples, eu vou somar o salário 's' + o aumento do salário.

#calcule 15% de aumento (de salários iguais ou menores que 1250) do valor que foi digitado em 's'
#o salário com aumento vai ser o salário antigo(s) mais 15% (s * 15/100) 
# salário antigo = (s)
# aumento = (s * 15/100)
# salário com aumento = s + (s * 15/100) 

# e vai ser da mesma forma para calcular os 10% de aumento para salários maiores que 1250.
#o salário com aumento vai ser o salário antigo(s) mais 10% (s * 10/100) 
# salário antigo = (s)
# aumento = (s * 10/100)
# salário com aumento = s + (s * 10/100) 

if s <= 1250:
    aumento = (s * 15 /100) + s 
else:
    aumento = (s * 10  /100) + s

#agora vai mostrar na tela o salário com o aumento de 15% para menores de 1250 e com 10$ de aumento para maiores de 1250
print('O funcionário que recebia {0:.2f} de salário, com o aumento vai receber {1:.2f}'.format(s,aumento))