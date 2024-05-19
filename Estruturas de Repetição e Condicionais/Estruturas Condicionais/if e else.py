# if / if... else / elif

MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CHN.")


if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade>=MAIOR_IDADE:
    print("Poder fazer aulas teóricas, mas não pode fazer aulas práticas.")

else:
    print("Ainda não pode tirar a CNH.")






