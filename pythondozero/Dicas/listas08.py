#crio uma lista chamada dados 
dados = list()
#adiciono o nome 'jake' e a idade 12 na lista 'dados' 
dados.append('jake')
dados.append(12)
#depois crio uma lista chamada pessoas 
pessoas = list()
#e adiciono a lista dados dentro da lista pessoas 
pessoas.append(dados)
#agora eu adiciono na posição 0 o nome john e na posição 1 a idade 22
dados[0] = 'john'
dados[1] = 22
#depois eu adiciono dentro de pessoas o que foi armazenado na lista dados, só que eu copio tudo usando
#o 'fatiamento' [:] >> copio do inicio ao fim, e depois mostro na tela  
pessoas.append(dados[:])
print(pessoas)


print('-' * 30)

#crio uma lista chamada galera e dentro dessa lista eu crio outras listas,
# onde os indices 0 1 2 3 representam cada uma das listas e o indice 0 e 1 representam os itens da lista.
# ex: print(galera[0][0]). dentro de galera, pegue a lista da posição 0 e mostre o itens 0 ('joão')   
galera = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])
print('-' * 30)
#posso criar um laço for para mostra todos os itens da lista 
#para cada pessoa dentro da lista galera, faça
for p in galera:
    print(p)

print('-' * 30)

#(eu posso mostrar o nome que está na posição 0 e posso mostrar a idade que está na posição 1)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')