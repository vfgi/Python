from veiculo import Veiculo
from carro import Carro


caminhao_rosa = Veiculo('rosa', 6, 'SCANIA', '10 lts')

print("Marca: ", caminhao_rosa.marca)
print("Cor: ", caminhao_rosa.cor)
print("Rodas: ", caminhao_rosa.rodas)
print("Tanque: ", caminhao_rosa.tanque)

print("")

carro_azul = Carro('azul', 4, 'bmw', 30)

print("Marca: ", carro_azul.marca)
print("Cor: ", carro_azul.cor)
print("Rodas: ", carro_azul.rodas)
print("Tanque: ", carro_azul.tanque)

carro_azul.abastecer(10)

carro_azul.abastecer(10)

print("Tanque: ", carro_azul.tanque)







# bi = input('digite algo: ')
#
# words = bi.split()
# letter = [word[0] for word in words]
#
#
# print(letter)
