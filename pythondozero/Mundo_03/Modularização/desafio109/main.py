# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

#importando o módulo 'moedas' 
import moedas

#pede um preço e preço e uma taxa
preco = float(input('Digite um preço: R$ '))
taxa = int(input('Digite a taxa: '))

#pergunto se o usuário quer formatar o preço, jogo a resposta pra maiúscula, elimino os espaços com strip e consido
#apenas o primeira caractere
show = str(input('Deseja formatar o preço? [S/N]: ')).upper().strip()[0]

#se show for igual a 'S'
if (show == 'S'):
    #show recebe true
    show = True
else:
    #senão, show recebe false 
    show = False

#depois, chamo os métodos do módulo 'moedas'
print(f'O dobro de {moedas.moeda(preco)} é {moedas.dobro(preco, show)}')
print(f'A metade de {moedas.moeda(preco)} é {moedas.metade(preco, show)}')
print(f'Aumentando {taxa}% , temos {moedas.aumentar(preco, taxa, show)}')
print(f'Diminuindo {taxa}% , temos {moedas.diminuir(preco, taxa, show)}')