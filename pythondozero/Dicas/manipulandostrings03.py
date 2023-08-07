#manipulando strings

#Fatiamento

#vamos começar fatiando uma string
# (lembrando que uma string é um sequecia de caracteres e os seus delimitadores especiais são as aspas simple ou duplas)
#a contagem começa sempre em 0
#vou pegar apenas a letra 's' que está na posição '3'
frase = 'Curso em Vídeo Python'
print(frase[3])

#inicie a contagem na posição 3('s') e pare na posição 13('o')
#obs: em uma contagem ele não considera o ultimo número, nesse exemplo a contagem começa no 3 e para no 13.
#só que ele não para no 13, ele para no 12 porque o ultimo número não é considerado
print(frase[3:13])

#agora eu vou pegar da letra s(que está  na posição 3) e vou até o final da string (na posição 21)
#print(frase[3:]) note que eu indiquei aonde a contagem(3) começa mas eu não indiquei aonde termina, 
#então a contagem vai até o final da string
print(frase[3:])

#como eu não indiquei aonde a contagem inicia, ela vai começar da posição 0, ou seja, o primeiro caractere('C') e, vai para na 
#posição que eu indiquei que nesse exemplo é 14. mas como o ultimo número não é considerado. então   a contagem para na posição 13
print(frase[:14])

#aqui eu estou indicando que a contagem inicia na posição 1 e para na 15(como o ultimo número não é considera para na posição 14)
#inicia no 1 termina no 15 e vai 'pulando' de 2 em 2  
print(frase[1:15:2])

#inicia na posição 1, não sei aonde termina(então vai até o final) e vai 'pulando' de 2 em 2 
print(frase[1::2])

#não sei em posição inicia(então inicia do primeiro caractere, a posição 0) e nem 
#em que posição termina(então vai até o ultimo caractere, a ultima posição), mas sei que vai 'pulando' de 2 em 2
print(frase[::2])

#uma dica abaixo para escrever um texto grande na tela
#não precisa usar o print em toda linha, tem um forma mais simples. veja abaixo
#basta utilizar as 3 aspas duplas ao invés de usar o print linha por linha
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")



#análise

#aqui eu estou pedindo para o computador contar quantas vezes a letra 'o' aparece na string 'Curso em Video Python'
#para isso eu uso o frase.count('letra ou palavra')
#no python tudo é um objeto então eu posso colocar qualquercoisa.algumacoisa
#é importante lembra que um 'O' maiúsculo não é a mesma coisa que um 'o' minúsculo
print(frase.count('o'))

#agora eu estou transformando toda string para letra maiúscula e eu estou pedindo para o computador contar
#quantas vezes a letra 'O' maiúscula aparece na string inteira 
#resumindo, transformei toda string para letra maiúscula. string antes de ser tranformada em maiúscula (sem o upper) >>> 'Curso em Video Python' 
# string depois de ser transformada em maiúscula (com o upper) >>> CURSO EM VIDEO PYTHON. 
# então, depois de ter transformado tudo para maiúsculo, eu quero contar quantas vezes a letra'O' maiúsculo aparece na string transformada(com upper)
print(frase.upper().count('O'))



#aqui eu estou pedindo para o computador procurar da posição 0 até a 13 quantas vezes a letra 'o' aparece
#lembre-se que num fatiamento a contagem inicia no 0 e o ultimo número vai ser ignorado. então na verdade vai do posição 0 até a 12 
print(frase.count('o', 0, 13))


#o len vai mostra qual é o comprimento da string
print(len(frase))

#o find vai mostrar em que posição o 'deo' inicia, nesse exemplo inicia na posição 11

print(frase.find('deo'))

#se o find não encontrar a posição que inicia a palavra 'android', ou se 'android' não existir dentro de 'frase' o find vai me retornar '-1'
#o -1 significa que a palavra que eu mandei ele encontrar (nesse exemplo é 'android') não existe dentro de 'frase'
print(frase.find('android'))

#aqui eu tô perguntando se existe a palavra 'Curso' dentro de 'frase'
#se existe ele me retorna - True
#se não existe ele me retorna - False
#aqui em baixo vai imprimir True
print('Curso' in frase)
#lembre-se que 'C' maiúsculo é diferente de 'c' minúsculo.
#aqui em baixo vai imprimir 'False'
print('curso' in frase)



#transformação

#aqui eu tô trocando a palavra 'Python' pela palavra 'Java'
#o replace faz essa substituição.
#para usar o replace digite:
#frase.replace('frase que eu quero substituir' , 'frase que vai substituir')
print(frase.replace('Python', 'Java'))

#strings são imutáveis. eu não posso fazer >>> frase[0] = 'j'

#o replace não muda a frase efetivamente, veja abaixo:
#frase = 'curso em video python' >>> não vai imprimir 'curso em video android' , vai imprimir 'curso em video python' 
#frase.replace('python, android') >>> eu não mandei substituir com o replace, eu mandei que nessa instância aqui ele substituisse, só que eu não mandei salvar os resultados.
#print(frase)   

#eu posso fazer com que imprimima 'curso em video android' salvando os dados dessa forma:
# frase = 'curso em video python'
# frase = frase.replace('python','android') 
#print(frase)
# agora sim eu consigo fazer uma alteração. agora vai imprimir curso em video android porque eu fiz a alteração e salvei os resultados.

#lembrando que uma string em seus microelementos, 
#ela é imutável, a não ser que eu utilize uma função de transformação de string e faça uma atribuição


#agora eu estou jogando tudo que está dentro de 'frase' para maiúsculo
print(frase.upper())

#agora tô jogando tudo que está dentro de 'frase' para minúsculo
print(frase.lower())

#o capitalize vai jogar tudo para minúsculo e vai deixar apenas o primeiro caractere em maiúsculo
#exemplo >>> Curso em video python
print(frase.capitalize())

#o title vai fazer o que o capitalize faz em todas as palavras da string. ele basicamente vai jogar tudo para minúsculo e vai deixar 
#apenas o primeiro caractere de cada palavra em maiúsculo.
# exemplo >>> Curso Em Video Python
print(frase.title())

#o strip remove os espaços da direita e da esquerda da string 
# por exemplo: '       curso em video python       '
# com o strip esses espaços seriam removido ' x x curso em video python x x '
# lstrip >>> remove apenas os espaços da esquerda e mantem os da direita ' x x curso em video python   '#
# rstrip >>> remove apenas os espaços da direita e mantem os da esquerda '   curso em video python x x '
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())

#divisão

#o split gera tecnicamente uma lista com todas as palavras numa cadeia de caracteres.
# o split vai separar palavra por palavra.
# exemplo >>>      frase = 'curso em video python'
#         >>>      print(frase.split())
#vai imprimir >>>  ['curso','em','video','python'] 
  
print(frase.split())

#junção

#quando eu tenho nome separado em lista eu consigo juntar um coisa com a outra.
#exemplo: aqui eu salvei o resultado.
#         >>>     frase = 'curso em video python'
#         >>>     frase = frase.split()
#         >>>     print('-'.join(frase))
# vai imprimir >>> curso-em-video-python 

# esse '-'.join(frase) significa que eu vou juntar todos os elementos de frase  ['curso','em','video','python'], utilizando esse separador '-'
#['curso','em','video','python'] juntando tudo isso com esse separador ficaria assim curso-em-video-python 


#aqui em baixo eu não salvei o resultado da alteração então vai imprimir
# C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n
print('-'.join(frase))
