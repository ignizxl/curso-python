

#ATENÇÃO: leiaDinheiro funciona, mas eu vou simplicar criando a função 'validaPreco'
#criando a função leia dinheiro que recebe uma mensagem como parÂmetro
def leiaDinheiro(mensagem):
    #criando algumas variáveis, todas iniciam valendo 0
    resultado = 0
    antesV = 0
    depoisV = 0
    auxiliar = 0
    #enquanto verdade, faça
    while True:
        #pede o preço, converte pra str e elimina os espaços 
        preco = str(input(mensagem)).strip()
        #se o preço for númerico, converto pra float, armazeno em resultado e uso o break pra encerrar 
        if (preco.isnumeric()):
            resultado = float(preco)
            break
        
        #se existir uma ',' no preco, faça
        elif(',' in preco):
            #auxiliar recebe o preco
            auxiliar = preco
            #preco recebe o preco, mas, sem a virgula 
            preco = preco.replace(',', '')
            #verifico se o preco sem a virgula é númerico, se for, faça
            if (preco.isnumeric()):
                #eu vou separar auxiliar(preco) pela virgula
                auxiliar = auxiliar.split(',')
                #na posição 0 eu tenho os números antes da virgula e na posição 1 eu tenho 
                #os número depois da  virgula 
                antesV = auxiliar[0]
                depoisV = auxiliar[1]
                #depois concateno o antes da virgula + '.' + depois da virgula e converto tudo pra float
                resultado = float(antesV + '.' + depoisV)
                #depois uso o break pra encerrar o laço 
                break
        
        #repito o mesmo processo aqui, a diferença é bem simples 
        elif('.' in preco):
            auxiliar = preco
            #retiro o '.' no preço e verifico se é um valor númerico, se for, faça 
            preco = preco.replace(',', '')
            if (preco.isnumeric()):
                #como já está com um '.', eu só converto o preço armazenado em auxiliar pra float
                #  e armazeno em resultado 
                resultado = float(auxiliar)
                #depois encerro o laço
                break

        else:
            #se nenhuma condição foi atendida, mostre um erro 
            print(f'Erro! "{preco}" não é um preço válido.')
    #retorne o resultado
    return resultado
        


def validaPreco(mensagem):
    #criando um variável chamada valido que inicia valendo false
    valido = False
    #enquanto valido não for verdadeiro, o while repete
    while not valido:
        #pede um entrada exibindo a mensagem que foi recebida como parâmetro, substitui as ',' por '.',
        #elimina os espaços da esquerda e da direita, converte tudo pra str e armazena tudo em entrada
        entrada = str(input(mensagem)).replace(',', '.').strip()
        #verifica se a entrada está vazia ou se a entrada é alfabética, se for, mostro um erro
        if (entrada.isalpha or entrada == ""):
            print(f'Erro! "{entrada}" não é um preço válido.')
        else:
            #senão, valido recebe verdadeiro e eu retorno a entrada convertida pra float 
            valido = True
            return float(entrada)