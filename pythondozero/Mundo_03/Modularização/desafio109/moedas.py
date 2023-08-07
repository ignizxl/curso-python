#criando os meus métodos

#ATENÇÃO NAS ALTERAÇÕES: em todas as funções, com exceção da função 'moeda', foi adicionado um parâmetro opcional chamado 'show'
#esse parâmetro opcional é do tipo 'boolean', quando ele é true, ele formata o preço e quando ele é false ele não 
#formata o preço

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


