import time

def abre_arquivo():
    try:
        arquivo = open('arquivo23.txt')
        return True
    except Exception as erro:
        print('Algo não está certo', erro)
        return False

while not abre_arquivo():
    print('tentando abrir arquivo')
    time.sleep(3)

print('Deu certo!!!')