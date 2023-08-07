# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento 
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO 
# nas eleições.


#criando a função voto 
def voto(anoDeNascimento):
    #utilizando o escopo de importação, ou seja, eu só estou importando a funcionalidade datetime dentro da
    #função voto, se eu tentar utilizar essa funcionalidade fora da função voto eu não vou conseguir 
    #Como eu só preciso dessa funcionalidade aqui dentro da função voto, eu só importo aqui dentro, dessa forma
    #eu economizo memória

    from datetime import datetime
    #pegando a data atual do sistema 
    dataAtual = datetime.now().year
    #para obter a idade, basta subtrair a dataAtual pela idade
    idade = dataAtual - anoDeNascimento
    #se a idade for menor que 16, voto negado
    if (idade < 16):
        return f'Com {idade} anos: Voto Negado!'
    #se a idade estiver entre 16 e 18 ou for maior que 65, voto opcional
    elif (16 <= idade < 18 or idade > 65):
        return f'Com {idade} anos: Voto Opcional!'
    #senão, voto obrigatório 
    else:
        return f'Com {idade} anos: Voto Obrigatório!'

print('-=' *15)
#pede o ano de nascimento 
anoDeNascimento = int(input('Em que ano você nasceu? '))
#chama a função voto passando o ano de nascimento
print(voto(anoDeNascimento))