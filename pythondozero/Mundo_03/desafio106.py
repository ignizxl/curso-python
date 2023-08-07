# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 


#criando uma função que cria uma titulo personalizado 
def tituloPersonalizado(titulo):
    #pega o tamanho do titulo, soma mais 4 e armazena em espaços
    espacos = len(titulo) + 4
    #multiplica o '=' pela quantidade de espaços
    print('=' * espacos)
    #exibe o titulo centralizado em x 'espaços'
    print(f'{titulo:^{espacos}}')
    print('=' * espacos)

#criando o menu
def menu():
    #enquanto verdade, faça
    while True:
        #chama a função titulo personalizado passando uma mensagem
        tituloPersonalizado("Sistema de Ajuda PyHelp")
        #pede o nome de função ou biblioteca
        x = input('Digite um nome de uma bibliote ou de um função para ver o manual (Digite "fim" para parar"): ').lower().strip()
        #se e x for igual a fim, uso o break pra encerrar o laço
        if (x == 'fim'):
            tituloPersonalizado('Encerrando!')
            break
        #senão, mostro titulo personalizado com o nome do comando 
        else:
            tituloPersonalizado(f'Acessando o manual do comando "{x}"')
            #e uso a função help para exibir o manual do comando digitado
            help(x)

#chamo o menu
menu()