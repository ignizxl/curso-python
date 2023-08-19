#importando tudo da biblioteca interface 
from lib.interface import *

#criando a função vefiricaArquivo
def verificaArquivo(nomeDoArquivo):
    try:
        #tento abrir o arquivo e ler o arquivo de texto
        #rt = read text ou ler texto
        arquivo = open(nomeDoArquivo, 'rt')
        #e depois fecho
        arquivo.close()
    
    #se essa exceção ocorrer, significa que o arquivo não foi encontrado 
    except (FileNotFoundError):
        #retorno false
        return False
    else:
        #se não hoube nenhuma exceção, retorno true
        return True

#criando a função para criar um arquivo
def criarArquivo(nomeDoArquivo):
    try: #tentando
        #criar um arquivo de texto, ('wt' é para criar um arquivo de texto)
        # e o '+', se por acaso não existir um arquivo de texto ele cria 
        #wt = writter text ou escrever texto 

        arquivo = open(nomeDoArquivo, 'wt+')
        #depois fecho o arquivo
        arquivo.close()
    except:
        #se houver qualquer exceção, vou mostrar um mensagem
        print('Houve um erro na criação do arquivo.')
    
    #senão, mostro uma mensagem de sucesso
    else:
        print(f"Arquivo '{nomeDoArquivo}' criando com sucesso! ")

#criando a função ler arquivo
def lerArquivo(nomeDoArquivo):
    try:
        #tento abrir o arquivo e ler o arquivo de texto
        arquivo = open(nomeDoArquivo, 'rt')
    except:
        #se ocorrer alguma exceção, mostro uma mensagem de erro
        print(f'Ocorreu um erro ao tentar ler o arquivo {nomeDoArquivo}')
    else:
        #senão
        #chamo a função cabecalho e passo a mensagem 'pessoas cadastradas'
        cabecalho('PESSOAS CADASTRADAS')
        # e por fim uso um for para ler as linhas do arquivo 

        # para cada linha do arquivo, eu faço
        for linha in arquivo:
            #eu splito a linha de acordo com o sinal ';' e armazeno em dados
            dados = linha.split(';')
            #dados na posição tem um '\n' que eu preciso remover deixar tudo formatado de maneira organizada
            #então pra isso eu faço, dados na posição 1 recebe dados na posição mas sem o '\n' que eu removi 
            #utilizando o replace, aonde tem '\n' eu substituo por ''
            dados[1] = dados[1].replace('\n', '')
            #e por fim, a cada iteração mostros dados na posição 0(nome) alinhado a esquerda em 30 espaços 
            #e mostro dados na posição 1(idade) alinha em 3 espaços a direita seguida de 'anos'
            print(f'{dados[0]:<30}{dados[1]:3>} anos')
            print()


    finally: 
        #e pra finalizar, se ocorrer um erro ou não, eu fecho o arquivo 
        arquivo.close()


#criando a função cadastrar pessoa que recebe 3 parÂmetros, o nome e a idade são parâmetros opcionais 
def cadastrarPessoa(nomeDoArquivo, nome = 'Desconhecido', idade = 0):
    try:
        #tento abrir o arquivo e adicionar 
        #at = append text ou adicionar texto 
        arquivo = open(nomeDoArquivo, 'at')
    
    except:
        #se houver exceção, mostro uma mensagem de erro
        print(f"Ocorreu um erro ao tentar abrir o arquivo '{nomeDoArquivo}'")
    
    else:
        #se tudo der certo
        try: #entro com outro try para tentar adicionar o nome e a idade 
            arquivo.write(f'{nome};{idade}\n')

        
        except:
            #se houver alguma exceção, mostro uma mensagem de erro 
            print('Ocorreu um erro ao tentar adicionar o novo cadastro!')
        
        else: #se tudo der certo, mostro uma mensagem de sucesso
            print(f"Novo resgistro de '{nome}' adicionado com sucesso!")
            #e por fim, fecho o arquivo 
            arquivo.close()