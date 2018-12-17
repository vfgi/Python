from conta import Conta
from client import Cliente

client1 = Cliente('Vitor', '371.002.988.06', 29)

print('Nome: ', client1.nome)
print('CPF: ', client1.cpf)
print('Idade: ', client1.idade)

conta1 = Conta('123', 50, 'R$ 1000,00')

print('Numero da conta: ', conta1.numero)
print('saldo em conta: R$ ', conta1.saldo)
print('limite da conta: ', conta1.limite)

conta1.sacar(30)

print('Saldo em conta: R$ ', conta1.saldo)

conta1.deposito(50)

print('Saldo em conta: R$ ', conta1.saldo)
