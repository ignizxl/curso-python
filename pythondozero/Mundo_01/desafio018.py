#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

#posso simplicar o import assim >>> from math import radians, sin, tan, cos
#com isso eu posso eliminar as referências 'math.' 
# lá no final do código tem uma forma simplificada



#para calcular o seno, cosseno e tangente eu vou importar umas funcionalidades da biblioteca  math
#peça pra o usuário digitar um ângulo e armazene o resultado em 'a' 
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
a = float(input('Digite um ângulo qualquer: '))

#agora eu vou converter o que foi armazenado em 'a'(o ângulo digitado) para radiano
# para isso eu crio a variável radians e já converto tudo que foi armazenado em 'a' para radiano. fiz isso pra não ter que 
# digitar a conversão de um por vez como está no exemplo abaixo:
# sen = math.sin(math.radians(a))
# cos = math.cos(math.radians(a))
# tan = math.tan(math.randians(a))

#pra resumir: vou pegar o ângulo que eu digitei e vou converter para radiano, vou pegar esse Ângulo
#convertido para radiano e vou calcular o seno dele. e vou fazer isso para o cosseno e a tangente
# tan = math.radians(a)) 

#para agilizar o processo, todo ângulo digitado em 'a' está sendo convertido para radiano e armazenado na variável 'radians'
radians = math.radians(a)

#agora é só  usar as funcionalidades para calcular seno, cosseno e tangente da variável 'radians'(que é onde está o ângulo de 'a' já convertido para radiano)
sen = math.sin(radians)
cos = math.cos(radians)
tan = math.tan(radians)



#agora vou imprimir na tela os resultados dos calculos de forma organizada.
print('O Ângulo de {0} tem o SENO de {1:.2f} \n O Ângulo de {0} tem o COSSENO de {2:.2f} \n O Ângulo de {0} tem a TANGENTE de {3:.2f}'.format(a, sen, cos, tan))








#importando de só as funcionalidades que eu preciso da biblioteca math
from math import radians, sin, cos, tan

#leia um Ângulo e armazene o resultado em 'a' 
a = float(input('Digite um ângulo qualquer: '))

#converta o ângulo digitado em 'a' para radiano e armazene o resultado em 'radians' 
radians = radians(a)

#efetue os calculos (usando funcionalidades de math) de seno, cosseno e tangente do novo ângulo armazenado em 'radians'
sen = sin(radians)
cos = cos(radians)
tan = tan(radians)
#agora mostre o resultados dos calculos do seno, cosseno e tangente
print('O Ângulo de {0} tem o SENO de {1:.2f} \n O Ângulo de {0} tem o COSSENO de {2:.2f} \n O Ângulo de {0} tem a TANGENTE de {3:.2f}'.format(a, sen, cos, tan))