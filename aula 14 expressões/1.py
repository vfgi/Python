import re
import requests

requisicao = requests.get('https://www.fcamara.com.br/')


string_de_teste = 'vou testar, testa, testo, teste os padrões tentando pegar somente meu e-mail que é ' \
                  'fernandes@fcamara.com'

padrao = re.search(r'\w\w\w\w\w.', string_de_teste)
padrao2 = re.findall(r'#\w+', requisicao.text)
padrao3 = re.findall(r'\w+@\w+.\w+.\w+', requisicao.text)

if padrao:
    print('padrao encontrado: ', padrao.group())
else:
    print('Padrão não encontrado')

if padrao2:
    print('padrao encontrado: ', padrao2)
else:
    print('Padrão não encontrado')

if padrao3:
    print('padrao encontrado: ', padrao3)
else:
    print('Padrão não encontrado')