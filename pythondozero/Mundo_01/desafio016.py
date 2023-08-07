#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#por ex: digite um número: 6.127
#o número 6.127 tem a parte inteira 6

#aqui eu estou pedindo para o computador ir na bliblioteca math, e importar somente a funcionalidade 'trunc'
#trunc --> vai eliminar a parte decimal(tudo depois do ponto)
from math import trunc

#pede pra o usuário digitar um valor  e depois armazena o resultado na variável 'n'
#o valor está sendo convertido para um número flutuante, como pede o enunciado
#como estamos trabalhando com números flutuantes é necessário fazer a conversão para float
n = float(input('Digite um valor: '))

#aqui eu uso o trunc para eliminar as casas decimais, para ficar somente a parte inteira
i = trunc(n)

#agora mostra na tela a porção inteira do número digitado acima.
print('o valor digitado foi {:.3f}, e a sua porção inteira é {}'.format(n, (i)))

#para ficar organizado eu digitei {:.3f} para deixar apenas 3 casas flutuantes depois do ponto


