
#criando a função acessarSite que recebe como parâmetro uma url
def acessarSite(url = ''):
    #importando a biblioteca urllib
    import urllib
    #importando o módulo interno request da biblioteca 'urllib'
    import urllib.request

    try:
        #tentado acessar a url
        #pra isso uso urllib.request.urlopen('endereço')
        acessando = urllib.request.urlopen(url)        
    #caso ocorra alguma exceção, retorne um erro
    except :
        return f"Erro: o endereço '{url}' está indisponível no momento!"

    else:
        #se tudo der certo, mostra um mensagem dizendo que o site está disponível
        return f"O endereço '{url}' está disponível!"
        
        