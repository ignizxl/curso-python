#tuplas(variáveis compostas)
#tuplas são variáveis que guardam vários valores

#exemplos:
#obs: toda tupla fica entre (). no python3.8 não é obrigatório colocar entre parenteses, mas eu vou usar entre () 
#no python eu posso iniciar as variáveis compostas de 3 formas 
#tuplas são imutavéis 

# () = tuplas
# [] = listas 
# {} = dicionários

#posições  >   0    >     1   >    2   >    3 
lanche = ('humbúrguer', 'suco', 'pizza', 'pudim') #pra pegar o primeiro elemento eu indico o indice do 0 
#posições     -4     <    -3   <  -2   <   -1 #pra pegar so ultimos elementos eu indico os  indices negativos iniciando do -1

#sempre que eu quiser printar na tela uma posição de um elemento eu preciso indicar  a posição entre []

print(lanche)
print(lanche[0]) #imprime humbúrguer
print(lanche[-2]) #imprime pizza
print(lanche[1:3]) #vai imprimir os do elemento 1 até o 2, lembre-se que o último número é ignorado
print(lanche[2:]) #vai do elemento 2 até o final, porque eu não indiquei o fim.
print(lanche[:2]) #inicia no primeiro elemento[que é o 0] e vai até o elemento 2 
print(lanche[-2:]) #inicia do elemento -2 e vai até o elemento -1 que é o ultimo

#imprimindo na tela utilizando o for 

print()
#cria um laço de repetição for do tamanho de lanche
#comida representa o indice, a cada iteração do for, comida vai sendo incrementado
#ex: repetição1 > comida = 0('humbúrguer')
#repetição2 > comida = 1 ('suco')
#repetição3 > comida = 2 ('pizza')
#repetição4 > comida = 3 ('pudim')
for comida in lanche: #dessa forma eu não posso indicar a posição 
    print(f'Vou comer {comida}')
print('comi demais!')

print()

#outra forma de fazer(posso indicar a posição)
#crio uma variável chamada indice, o for vai repertir de acordo com o tamanho do len(lanche), isto é, vai repetir o comprimento de lanche
for indice in range(0, len(lanche)):
    #aqui eu vou comer o lanche e indico a posição do meu indice
    print(f'Vou comer {lanche[indice]} que está na posição {indice}')
print('comi demais!')

print()

#outra forma de fazer 

#posições  >   0    >     1   >    2   >    3 
#lanche = ('humbúrguer', 'suco', 'pizza', 'pudim')
#crio uma variável chamada posição(meu indice), crio uma variável comida que vai representar o que foi enumerado de lanche)
#e enumerate(lanche) vai numerar o lanche(0 = 'humbúerguer' , 1 = 'suco', 2 = 'pizza' , 3 = 'pudim')
for posicao, comida in enumerate(lanche):
    print(f'vou comer{[comida]} na posição {posicao}')
print('comi demais!')

print()


a = (2, 5, 4) #crio a tupla só com valores númericos 
b = (5, 8, 1, 2) #crio b tupla só com valores númericos
c = a + b #concatena a tupla a + a tupla b
print(a) #imprime a normal
print(b)# imprime b normal
print(c) #imprime a concatenado com b 

print(sorted(c)) #o sorted imprime de maneira organizada, se for palavras, ele imprime em ordem alfabética e se for número ele imprime
#em ordem crescente 
print(len(c)) #retorna o tamanho de c, ou seja quantos elementos 'c' possui 
print(c.count(5)) #o count, conta quantas vezes o 5 aparece
print(c.index(8))#mosta em qual posição o número 8 está. detalhe, ele mostra a primeira ocorrência
print(c.index(5, 2))#mostra em qual posição o 5 está, iniciando da segunda posição 

#no python eu posso ter variós tipos de dados dentro de uma tupla 
#veja o exemplo a seguir 
#eu tenho dados do tipo str, int e float em uma única tupla 
pessoa = ('joão igor', 'Masculino', 18, 1.70)
print(f'Olá {pessoa[0]}, você é do sexo {pessoa[1]}, tem {pessoa[2]} anos e mede {pessoa[3]}m de altura.')