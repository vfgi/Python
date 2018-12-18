import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/')
    cotacao = json.loads(requisicao.text)

    print('### COTAÇÃO ###', datetime.datetime.now())
    print(cotacao)
    time.sleep(4)