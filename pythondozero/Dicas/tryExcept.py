
#tratamento de erros 

#estrutura:
#try:
#    ... O try vai tentar realizar alguma ação

#except:
#    ... Se o try falhar, significa que ocorreu alguma exceção, aconteceu algum erro...

#else:
#    ... Vai entrar no else se não houver nenhuma exceção

#finally:
#    ... O finally sempre vai acontecer, mesmo se houver ou não alguma exceção  


#OBS: else e finally são opcionais 


#exemplos práticos

try:
    #o try vai tentar realizar essa operação...
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

#explicitando o tipo de exceção...
#se ocorrer um erro com o tipo de dados, vai exibir uma mensagem... se ocorrer um erro por uma divisão por zero
#vai exibir outra mensagem.. e por aí vai 
except (TypeError, ValueError):
    print('Tivemos um problema com o tipo de dados que você digitou! ')   

except (ZeroDivisionError):
    print('Não é possível dividir um número por zero! ')

except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados! ')

#eu também posso formatar as exceções 
except Exception as erro:
    #e mostrar a causa do erro por exemplo...
    print(f'Causa do erro: {erro.__cause__}')
    print(f'Classe do erro: {erro.__class__}')

#se não ouver nenhum erro de operação durante o 'try', vai exibir o resultado, caso contrário, vai exibir 
#alguma das exceções acima
else:
    print(f'O resultado é {r:.2f}')
#e o finally sempre irá acontecer, mesmo se houver ou não alguma exceção..
finally:
    print('Volte sempre!')