# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em
# um arquivo de texto simples. O sistema só vai ter duas opções: Cadastrar uma nova pessoa e 
# lista as pessoas cadastradas.

#importo tudo da biblioteca 'interface' e da biblioteca 'arquivo'
from lib.interface import *
from lib.arquivo import *
#da biblioteca time, importo a funcionalidade sleep 
from time import sleep


arquivo = 'cursoemvideo.txt'
#chamando a função verifica arquivo para verificar se o arquivo 'cursoemvideo.txt' existe
if (not verificaArquivo(arquivo)):
   #se o arquivo não existir, chamo a função criarArquivo
   criarArquivo(arquivo)



#chamando a função cabecalho e passando o titulo do sistema
cabecalho('SISTEMA ARQUIVO v1.0')

while True:
    #criando a variável resposta, que recebe a chamada da função menu com as opções abaixo(ver, cadastrar e sair)
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    #verificando se a opção é válida 
    if (resposta == 1):
        #chamando a função ler arquivo
        lerArquivo(arquivo)

    elif (resposta == 2):
        #chamando a função cabecalho passando o 'texto' 'NOVO CADASTRO'
        cabecalho('NOVO CADASTRO')
        #pede o nome, converte pra str, uso  a title pra deixa a primeira letra de cada nome maiúscula
        nome = str(input('Nome: ')).title()
        #chamo a função leiaInt pra validar a idade 
        idade = leiaInt('Idade: ')
        #chamando a função cadastrarPessoa
        cadastrarPessoa(arquivo, nome, idade)

    elif (resposta == 3):
        #se 'resposta' for igual a 3, mostro um mensagem e uso o break pra encerrar o laço
        loading()
        cabecalho(' << Volte Sempre! >>')
        loading()
        break
    
    else:
        #se 'resposta' não for válida, mostra um mensagem de erro, espera 1.5 seg e chama a função loading
        print('Erro: Digite um opção válida!')
        sleep(1.5)
        loading()