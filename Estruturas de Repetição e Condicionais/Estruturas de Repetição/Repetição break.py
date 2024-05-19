# Estrutura de Repetição break:

# while True:
#    opcao = int(input("Informe um número: "))

#    if opcao == 10:
#        break

    # print(opcao)


# o comando break irá parar o laço enquanto o comando continue irá pular a execução.

for numero in range(100):

    if numero % 2 == 0: # aparecer apenas os número ímpares.
        continue # Este comando faz com que elimine o número da sequência que inserimos logo acima.

    print(numero, end=" ")