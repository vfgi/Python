import requests

cabecalho = {'user-agente': 'windows 12'}

dados = {'username': 'Vitor',
         'password': 'vitor123'}
try:
    requisicao = requests.post('https://putsreq.com/ntcEcGEr6EDaCRM2eU9a',
                               headers=cabecalho,
                               data=dados)
    texto = requisicao.text
except Exception as e:
    print('Erro de requisição: ', e)

print(texto)