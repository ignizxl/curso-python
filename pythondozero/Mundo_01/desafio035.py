#desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 


#para dar uma melhorada na aparência do programa vou imprimir 30 vezes na tela os simbolos de '=-='
print('=-=' * 30)
print('Analisador de triângulos')
print('=-=' * 30)

#agora vou pedir ao usuário o comprimento dos 3 segmentos e vou armazenar os resultados em s1, s2 e s3
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: ')) 
s3 = float(input('Digite o terceiro segmento: '))


#para formar um triângulo, a soma do s1 + s2 tem que ser maior do que o s3.
#posso fazer isso de varias formas 
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('os segmentos acima podem formar um triângulo')

# segunda forma. em alguns casos funciona. 
#if s1 + s2 > s3:
#    print('Os seguimentos acima PODEM formar um triângulo.')


#joguei o s1 s2 e s3 dentro de uma lista.
# l = [s1,s2,s3]

# #agora vou verificar se a soma de s1 + s2 + s3 - o maior da lista, é maior que o maior da lista.
# #eu estou pegando os dois menores segmentos da lista e estou somando eles, se a soma dos dois menores segmentos da lista 
#for maior que o maior segmento da lista, então é possivel formar um triângulo
# if s1 + s2 + s3 - max(l) > max(l):
#     print('Os seguimentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')