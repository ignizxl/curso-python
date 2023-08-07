# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
# "a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ")

#criando a função leiaInt que recebe como parâmetro um mensagem 
def leiaInt(mensagem):
    #criando um variável 'valor' que inicia valendo 0 
    valor = 0

    #enquanto verdade, faça 
    while True:
        #pede um número através de um input mas exibindo a mensagem que foi passada como parâmetro na função 
        #leiaInt
        n = str(input(mensagem))
        #verifica se o que foi digitado é númerico
        if (n.isnumeric()):
            #se for, converto o n pra int e armazeno em valor  
            valor = int(n)
            #e encerro o laço com o break
            break
        #senão
        else:
            #mostra um mensagem de erro
            print('Erro! Digite um número inteiro válido.')

    #depois de ter validado a resposta, retorno o valor 
    return valor
#chama a função leiaInt passando o mensagem 'Digite um número: '
n = leiaInt('Digite um número: ')
#esse print só vai acontecer quando o usuário passar um número inteiro  
print(f'Você digitou o número "{n}"')
