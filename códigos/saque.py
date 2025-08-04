import time

realizar_saque = True
verif_saque = True

notas_reg = [100, 50, 20, 10, 5, 2, 1]

def calc_saque(valor):
    array = []
    for notas in range(6):
        try:
            qntd = valor // notas_reg[notas]
            array.append(qntd)
            valor %= notas_reg[notas]
        except ValueError:
            continue
    return array

while realizar_saque:

    result = []

    while verif_saque:

        try:
            valor_desejado = float(input("\nDigite o valor desejado de saque: R$ "))
            break

        except ValueError:
            print("\nO valor digitado é inválido!")

    result = calc_saque(valor_desejado)

    print("\nO saque realizado foi de:")
    for notas in range(6):
        print(f"\n{notas}. {int(result[notas])} notas de R${notas_reg[notas]}")

    if input("\nDeseja realizar outro saque (S/N)? ").lower() != 's':
        print("\nMuito bem! Encerrando o programa...\n")
        time.sleep(1)
        realizar_saque = False
        break



    