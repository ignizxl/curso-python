#import ---> importa todas as funcionalidades (generalista)
#from ... import ... ---> importa apenas as funcionalidades que eu quero (especifico)

#por exemplo:

#eu estou importando todas as funcionalidades da biblioteca 'math'
import math 

#pede um valor ao usuário e armazena o resultado em 'num'
num = float(input('Digite um valor: '))

#agora calcule a raiz quadrada do valor armazenado em 'num'. para calcular raiz utilize a funcionalizade(isqrt) da biblioteca 'math'
#para importar a funcionalidade digite: math.'nome da funcionalidade'('nome da variável')
raiz = math.sqrt (num)

#escreva na tela o resultado do calculo da raiz quadrada do valor armazenado em 'num'
print('A raiz quadrada de {} é {}'.format(num, raiz))

#eu também posso utilizar funcionalidade dentro do .format
#print('A raiz quadrada de {} é {}'.format(num, math.ceil(raiz)))




#a segunda forma de importar é usando o from ... import ... essa é uma forma mais especifica de importar um ou mais funcionalidades


#eu estou importando apenas duas  funcionalidades da biblioteca 'math'
#sqrt --> calcula raiz quadrada
#ceil --> arredonda o número pra cima. por ex: o número 7.8 arredondado pra cima fica 8.0

#para importar de forma especifica digite:
#from 'nome da biblioteca' import 'nome da funcionalidade'
from math import ceil, sqrt

#pede um valor ao usuário e armazena o resultado em 'num'
num = float(input('Digite um valor: '))

#agora calcule a raiz quadrada do valor armazenado em 'num'. para calcular raiz utilize a funcionalizade(isqrt) da biblioteca 'math'
#para importar a funcionalidade digite: math.'nome da funcionalidade'('nome da variável')
#como eu estou usando o from import eu não preciso usar o math. , agora em vez do math.'nome da funcionalizade'(nome da variável)
#eu uso apenas --> 'nome da funcionalidade'(nome da variável)
raiz = sqrt (num)

#escreva na tela o resultado arredondado pra cima do calculo da raiz quadrada do valor armazenado em 'num'
#eu também posso usar a funcionalidade dentro do .format
print('A raiz quadrada de {} é {}'.format(num, ceil(raiz)))

