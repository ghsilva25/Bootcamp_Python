
# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True)
print(True and False)
print(True or True)
print(False or False)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True


saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)



