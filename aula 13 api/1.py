import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=b7d5c054')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('erro na conexão')
        return None

def printar_detalhes(filme):
    print('Titulo: ', filme['Title'])
    print('Atores: ', filme['Actors'])
    print('Data de Lançamento: ', filme['Released'])
    print('Gênero: ', filme['Genre'])
    print('Nota: ', filme['imdbRating'])


sair = False

while not sair:
    nome = input('Digite o Titulo do Filme ou sair para fechar: ')

    if nome == sair:
        sair = True
    else:
        filme = requisicao(nome)
        if filme['Response'] == False:
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)

