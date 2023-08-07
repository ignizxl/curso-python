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

#criando a função linha que recebe um parâmetro (opcional)
def linha(tamanho = 42):
    #retorna o tamanho(parÂmetro opcional que é 42) vezes o sinal '-'
    return tamanho * '-'

#criando a função cabecalho que recebe como parâmetro um texto
def cabecalho(txt):
    #chama função linha
    print(linha())
    #centraliza o texto em 42 espaços
    print(f'{txt:^42}')
    #chama função linha
    print(linha())

#criando a função menu que recebe como parâmetro uma lista de opções
def menu(listaDeOpcoes):
    #chama a função cabecalho passando o texto 'MENU PRINCIPAL'
    cabecalho('MENU PRINCIPAL')

    # cont = 1
    # for item in listaDeOpcoes:
    #     print(f'{cont} - {item}')
    #     cont += 1
   
   #criando um for e usando a função enumerate para percorrer cada elemento dentro da lista de opções
    for index, item in enumerate(listaDeOpcoes):
        #index (somo +1 pra exibir 1 2 e 3 ao invés de 0 1 e 2) representa a posição
        #e o item representa a 'opção da vez'
        print(f'{index + 1} - {item}')

    #chamo a função linha
    print(linha())

    #chamo a função leia int pra fazer a validação da opção 
    opcao = leiaInt('Sua opção: ')
    return opcao


def loading():
    #multiplo os sinais '-=' vezes 21 e armazeno tudo em 'line' 
    line = '-=' * 21

    #crio um for para percorrer cada sinal armazenado dentro de 'line' 
    for i in line:
        from time import sleep
        #a cada iteração do for, eu uso a função sleep para esperar 0.01 segundo antes de imprimir o 'i' 
        sleep(0.01)
        #mostro o 'i'(sinal), uso o end para continuar na mesma linha e uso também o flush = true
        #quando o 'flush' é true, a funcionalidade sleep vai funcionar da maneira que eu quero,
        #esperando 0.01 segundos e imprimindo o sinal a cada iteração do for, ou seja, a cada iteração
        #você vai ver uma 'linha' sendo formada como uma barra de 'loading'. Agora se o flush é false,
        #você não conseguie acompanhar essa linha sendo formada, você só vê o resultado final, que é 
        #a linha já foi toda 'formada', por assim dizer.
        # flush = true; a cada iteração do laço, 'espera' alguns segundos e printa o 'i'
        # flush = false; a cada iteração do laço, 'espera' alguns segundos mas não mostra o 'i', só mostra tudo
        # assim que o laço acabar 
        print(f'{i}', end = '', flush = True)
    print()