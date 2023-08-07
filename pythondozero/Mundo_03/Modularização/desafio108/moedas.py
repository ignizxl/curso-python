#criando os meus métodos

#dobro, que recebe um valor opcional como parâmetro
def dobro(valor = 0):
    #multiplica o valor por 2, armazena em resultado e depois retorna resultado
    resultado = valor * 2
    return resultado

#metade, que recebe um valor opcional como parâmetro
def metade(valor):
    #divide o valor por 2, armazena em resultado e depois retorna resultado
    resultado = valor / 2
    return resultado

#aumentar, que recebe um valor opcional e uma taxa (opcional)
def aumentar(valor = 0, taxa = 0):
    #divido a taxa por 100 e depois multiplico pelo valor e armazeno tudo em aumento 
    aumento = valor * (taxa / 100)
    #depois somo o valor mais o aumento, armazeno em resultado e depois retorno o resultado 
    resultado = valor + aumento
    return resultado

#diminuir, que recebe um valor e uma taxa (opcional)
def diminuir(valor = 0, taxa = 0):
    #divido a taxa por 100 e depois multiplico pelo valor e armazeno tudo em diminuir 
    diminuir = valor * (taxa / 100)
    #depois, vou subtrair o valor por 'diminuir' e armazena tudo em resultado
    resultado = valor - diminuir
    #e por fim, retorno o resultdado 
    return resultado


#ATENÇÃO: está função abaixo funciona, mas vou simplificar
# def moeda(valor = 0):

#     formatacao = f'R${valor:.2f}'
#     resultado = ''
#     for i in formatacao:
#         if (i == '.'):
#             i = ','
#         resultado += i

#     return f'{resultado}'

#criando a função moeda que recebe um preço (opcional)
def moeda(preco = 0, moeda = 'R$'):
    #formato o preço com 2 casas flutuantes e utilizo o replace para substituir todos os '.' por ','
    # e por fim, armazeno tudo em formatação 
    formatacao = f'{moeda}{preco:.2f}'.replace('.', ',')
    #retorno a formatação
    return formatacao