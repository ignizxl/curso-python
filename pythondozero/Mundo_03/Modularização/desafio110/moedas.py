#criando os meus métodos

#ATENÇÃO NAS ALTERAÇÕES: adicionei uma nova função chamada 'resumo' 

#criando a função moeda que recebe um preço (opcional)
def moeda(preco = 0, moeda = 'R$'):
    #formato o preço com 2 casas flutuantes e utilizo o replace para substituir todos os '.' por ','
    # e por fim, armazeno tudo em formatação 
    formatacao = f'{moeda}{preco:.2f}'.replace('.', ',')
    #retorno a formatação
    return formatacao

#dobro, que recebe um valor opcional como parâmetro, e parâmetro show (opcional)
def dobro(valor = 0, show = False):
    #multiplica o valor por 2, armazena em resultado e depois retorna resultado
    resultado = valor * 2
    #verifica se show é true 
    if (show):
        #se for, chamo a função moeda no 'resultado' para formatar o preço 
        resultado = moeda(resultado)

    #outras maneiras de fazer essa vericação é assim:
    # return resultado if show is False else return moeda(resultado)
    # return resultado if not show else moede(resultado)

    return resultado

#metade, que recebe um valor opcional como parâmetro, e parâmetro show (opcional)
def metade(valor, show = False):
    #divide o valor por 2, armazena em resultado e depois retorna resultado
    resultado = valor / 2

    if (show):
        resultado = moeda(resultado)

    return resultado


#aumentar, que recebe um valor opcional e uma taxa (opcional), e parâmetro show (opcional)
def aumentar(valor = 0, taxa = 0, show = False):
    #divido a taxa por 100 e depois multiplico pelo valor e armazeno tudo em aumento 
    aumento = valor * (taxa / 100)
    #depois somo o valor mais o aumento, armazeno em resultado e depois retorno o resultado 
    resultado = valor + aumento

    if (show):
        resultado = moeda(resultado)

    return resultado

#diminuir, que recebe um valor e uma taxa (opcional), e parâmetro show (opcional)
def diminuir(valor = 0, taxa = 0, show = False):
    #divido a taxa por 100 e depois multiplico pelo valor e armazeno tudo em diminuir 
    diminuir = valor * (taxa / 100)
    #depois, vou subtrair o valor por 'diminuir' e armazena tudo em resultado
    resultado = valor - diminuir
    #e por fim, retorno o resultdado 

    if (show):
        resultado = moeda(resultado)

    return resultado


#criando a função resumo que recebe 4 parâmetros opcionais (preco, aumento, redução e show)
def resumo(preco = 0, taxaAumento = 10, taxaReducao = 5, show = True):
    #para deixar o programa organizado eu mostro um titulo personalizado e centralizado em 33 espaços
    print('-' * 33)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 33)

    #e por fim, chamo as funções moeda, dobro, metade, aumentar e diminuir, passando como parâmetro
    #os parâmetros recebidos acima. mostro tudo centralizado a esquerda em 15 espaços
    #\t = é uma tabução
    print(f'Preço analisado: \t{moeda(preco):<15}')
    print(f'Dobro do preço: \t{dobro(preco, show):<15}')
    print(f'Metade do preço: \t{metade(preco, show):<15}')
    print(f'{taxaAumento}% de aumento: \t\t{aumentar(preco, taxaAumento, show):<15}')
    print(f'{taxaReducao}% de redução: \t\t{diminuir(preco, taxaReducao, show):<15}')

    print('-' * 33) 