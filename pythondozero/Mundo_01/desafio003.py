#crie um script Python que leia dois números e tente mostrar a soma entre eles.
#como eu preciso somar dois números eu devo fazer a conversão para o resultado do input(tudo que tá dentro do input é string) ser um resultado inteiro
#para fazer a conversão eu digito int na frente do input. dessa forma --> int(input'...')) 

print('Exemplo - 1 \n Somando os números')
#pede para o usuário digitar um número e armazena o resultado no n1
num1 = int(input('Digite um número: '))
#pede para o usuário digitar outro número e armazena o resultado no n2
num2 = int(input('Digite outro número: '))

#agora eu criei uma variável chamada 'soma' que vai somar os valores que foram armazenados em 'n1' e 'n2' 
soma = num1 + num2

#agora vai escrever na tela o resultado da soma entre 'n1' + 'n2' 
print(f'A soma entre {num1} + {num2} é igual a {soma}')






print('Exemplo - 2 \n Concatenando os números')
#se eu não fizer a conversão para 'int' eu vou estar concatenando o valor de 'n1' + 'n2', ou seja, eu vou estar juntando os valores
#por ex:
#pede para o usuário digitar um número e armazena o resultado no n1
n1 = (input('Digite um número: '))
#pede para o usuário digitar outro número e armazena o resultado no n2
n2 = (input('Digite outro número: '))

#agora eu criei uma variável chamada 'soma' que vai concatenar os valores que foram armazenados em 'n1' e 'n2' 
concatenacao = n1 + n2

#agora vai escrever na tela o resultado da concatenação entre 'n1' + 'n2' 
print(f'A concatenação entre {n1} + {n2} é igual a {concatenacao}')

#se eu digitar n1 = 4 
#e n2 = 4
#o resultado não vai ser 8. o resultado vai ser 44 porque eu estou somando(concatenando) duas strings (isso acontece porque a conversão
#não foi feita) 

#a soma entre strings é chamada de concatenação