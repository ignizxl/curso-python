# Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#importando as funções leiaInt e leiaFloat do 'módulo' 'metodos'
from metodos import leiaInt, leiaFloat

#chamando as funções
inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')

#mostrando o número inteiro digitado e o número real digitado 
print(f"O número inteiro digitado foi '{inteiro}' e o número real digitado foi '{real}'")