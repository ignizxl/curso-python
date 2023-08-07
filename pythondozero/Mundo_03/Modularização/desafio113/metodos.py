#criando a função leiaInt
def leiaInt(msg):
    #enquanto verdade, faça
    while True:

        try: #tentando...
            #pede um número, converte pra int e armazena em num
            num = int(input(msg))
            
        #se o usuário interromper o teclado, mostre uma mensagem e retorne zero
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar nenhum número!')
            
            return 0
        #se ocorrer qualquer outrar exceção, mostre um mensagem de erro
        except:
            print('Erro! Digite um número inteiro válido')

        #se não houver nenhuma exceção, retorne num 
        else:
            return num
    

#criando a função leiaFloat (obs: eu poderia simplesmente copiar a função 'leiaInt', mas acabei preferindo
# fazer de outra forma) 
def leiaFloat(msg):
    #criando uma variável chamada 'valido' que inicialmente é 'false'
    valido = False
    #enquanto valido não for 'true', o while repete
    while (not valido):
        
        try: #tentando ..
            #pede um número, converte pra float e armazena em num
            num = float(input(msg))
            #e já tento fazer 'valido' receber 'true', e isso só vai acontecer se o número digitado
            #for float, ou melhor, só vai acontecer se não ocorrer nenhuma exceção 
            valido = True
        
        #se o usuário interromper o teclado, exibe um mensagem e depois retorna 0
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar nenhum número!')
            return 0
        #se ocorrer qualquer outra exceção, vai exibir um mensagem 
        except:
            print('Erro! Digite um número real válido')
    #e por fim, depois de ter validado tudo, retorno num 
    return num