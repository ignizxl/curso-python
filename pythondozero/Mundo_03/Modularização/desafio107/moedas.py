#criando os meus métodos

#dobro, que recebe um valor como parâmetro
def dobro(valor):
    #multiplica o valor por 2, armazena em resultado e depois retorna resultado
    resultado = valor * 2
    return resultado

#metade, que recebe um valor como parâmetro
def metade(valor):
    #divide o valor por 2, armazena em resultado e depois retorna resultado
    resultado = valor / 2
    return resultado

#aumentar, que recebe um valor e uma taxa (opcional)
def aumentar(valor, taxa = 10):
    #divido a taxa por 100 e depois multiplico pelo valor e armazeno tudo em aumento 
    aumento = valor * (taxa / 100)
    #depois somo o valor mais o aumento, armazeno em resultado e depois retorno o resultado 
    resultado = valor + aumento
    return resultado

#diminuir, que recebe um valor e uma taxa (opcional)
def diminuir(valor, taxa = 10):
    #divido a taxa por 100 e depois multiplico pelo valor e armazeno tudo em diminuir 
    diminuir = valor * (taxa / 100)
    #depois, vou subtrair o valor por 'diminuir' e armazena tudo em resultado
    resultado = valor - diminuir
    #e por fim, retorno o resultdado 
    return resultado