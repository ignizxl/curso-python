# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

#importando o módulo 'moedas' 
import moedas

#pede um preço e preço e uma taxa
preco = float(input('Digite um preço: R$ '))
taxa = int(input('Digite a taxa: '))
#depois, chamo os métodos do módulo 'moedas'
print(f'O dobro de {preco:.1f} é {moedas.dobro(preco):.1f}')
print(f'A metade de {preco:.1f} é {moedas.metade(preco):.1f}')
print(f'Aumentando {taxa}% , temos {moedas.aumentar(preco, taxa):.1f}')
print(f'Diminuindo {taxa}% , temos {moedas.diminuir(preco, taxa):.1f}')