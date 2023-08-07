# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

#importando o módulo 'moedas' 
import moedas

#pede um preço e preço e uma taxa
preco = float(input('Digite um preço: R$ '))
taxa = int(input('Digite a taxa: '))
#depois, chamo os métodos do módulo 'moedas'
print(f'O dobro de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco))}')
print(f'A metade de {moedas.moeda(preco)} é {moedas.moeda(moedas.metade(preco))}')
print(f'Aumentando {taxa}% , temos {moedas.moeda(moedas.aumentar(preco, taxa))}')
print(f'Diminuindo {taxa}% , temos {moedas.moeda(moedas.diminuir(preco, taxa))}')