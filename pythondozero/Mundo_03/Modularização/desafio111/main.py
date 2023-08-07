# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 
# para o primeiro pacote e mantenha tudo funcionando.

#neste desafio, eu apenas estruturei os diretórios e os arquivos.py

#do módulo 'utilidadesCEV' eu importo apenas a biblioteca 'moedas'
from utilidadesCEV import moedas

#pede um preço e preço e uma taxa
preco = float(input('Digite um preço: R$ '))
aumento = int(input('Digite a taxa de aumento: '))
reducao = int(input('Digite a taxa de redução: '))

#utilizando o método 'resumo' da biblioteca 'moedas'
moedas.resumo(preco, aumento, reducao)