#refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# equilátero: todos os lados iguais
# isósceles: dois lados iguais
# escaleno: todos os lados diferentes # 


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
#agora vou criar um if dentro de outro if. >>> if pode formar um triângulo? sim. 
#  se pode formar um triângulo me diga qual tipo de triângulo que pode formar. note que são duas condições, por isso if dentro de if. 
#eu nunca posso começar com um elif ou com o else. sempre comece com um if

#pra formar um equilátero todos os lados devem ser iguais. eu posso fazer de outra forma 
#if s1 == s2 and s2 == s3 and s1 == s3: 

    if s1 == s2 == s3:
        print('O triângulo que pode ser formado é o EQUILÁTERO .')
#para forma um escaleno, todos os lados devem ser diferentes
#elif s1 != s2 and s2 != s3 and s1 != s3:
# mais uma vez eu posso fazer de outra forma
#s1 diferente de s2, s2 diferente de s3 e s3 diferente de s1.
    elif s1 != s2 != s3 != s1:
        print('O triângulo que pode ser formado é o ESCALENO.')
#e na ultima condição, eu vou usar o else, porque se não for equilátero ou escaleno, só pode ser isósceles, por isso que eu uso o else 
    else: 
        print('O triângulo que pode ser formado é o ISÓSCELES')



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

