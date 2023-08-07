# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
# e fechados na ordem correta.

#pede pra o usuário digitar uma espressão qualquer, elimina os espaços converte pra str e armazena em expressão 
expressao = str(input()).strip()
#cria um variável chamada left que vai usar a função count para contar todos os parenteses apontados para esquerda >>> (
left = expressao.count('(')
right = expressao.count(')')
#cria a variável valida que recebe o que foi armazenado em left + o que foi armazenado em right 
valida = left + right
#se você abre um parenteses você precisa fecha-lo. então, o número de parenteses sempre será um número par
#então eu faço a verificação, se o resto da divisão da variável valida por 2 for igual a zero, ela é valida, senão, ela vai ser um número impar e não vai ser valida 
if valida % 2 == 0:

    print('expressão valida')
else:
    print('expressão invalida')

### outra forma de fazer, essa está 'mais correta'

#pede pra o usuário digitar uma expressão e armazena em 'expressao'
expressao = str(input('Digite a expressão: '))
#crio uma lista chamada pilha que inicia vazia 
pilha = []
#inicio um laço for, para cada simbolos dentro de expressão 
# (eu vou usar o laço for para 'varrer' toda a expressão do inicio ao fim para contar os parenteses abrindo 
# e os parenteses fechando)
for simbolos in expressao:
    #se o simbolo for igual a o parenteses abrindo, faça
    if simbolos == '(':
        #eu uso o append para adicionar o parenteses na pilha
        pilha.append('(')
    #se simbolos for igual um parenteses fechando, faça
    elif simbolos == ')':
        #se o tamanho da lista for maior do que zero, significa que já tem um parenteses aberto dentro da pilha
        #então eu vou remove-lo da pilha, porque o parenteses já encontrou o seu par, ou seja ao invés de adicionar )
        #  eu vou remover o ( que já está lá dentro da pilha
        if len(pilha) > 0:
            pilha.pop()
        #senão
        else:
            #se cair no else, significa que a lista está vazia, então eu adiciono o sinal de parenteses fechando, se o primeiro sinal for 
            #um parenteses fechando e depois um abrindo )( dessa forma a expressão já está errada, então eu adiciono o primeiro sinal ) na pilha
            #indicando um fechamento sem abertura  #e uso o brak para encerrar o laço
            pilha.append(')')

            break
#se a minha pilha estiver vazia, significa que a expressão está correta, porque cada vez que eu acho um parenteses abrindo
#  eu adiciono na pilha e cada vez que eu acho um parenteses fechando eu removo o que já estava dentro da pilha porque o parenteses
# que estava abrindo achou o seu fechamento ou seja ele achou o seu 'par' (abriu e fechou). por isso que para a expressão ser válida
# a pilha precisa estar vazia  
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')