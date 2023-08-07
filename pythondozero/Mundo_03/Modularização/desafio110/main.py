# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

#importando o módulo 'moedas' 
import moedas

#pede um preço e preço e uma taxa
preco = float(input('Digite um preço: R$ '))
aumento = int(input('Digite a taxa de aumento: '))
reducao = int(input('Digite a taxa de redução: '))

moedas.resumo(preco, aumento, reducao)