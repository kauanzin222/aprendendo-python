import time

while True:
    try:
        palavra = input("\nInforme uma palavra: ").strip().lower()
        
        if not(palavra.isalpha()):
            print("Palavra inválida! Tente novamente.")
            continue

    except ValueError:
        print("Palavra inválida! Tente novamente.")

    plvrInvertida = palavra[::-1]

    if palavra == plvrInvertida:
        print("\nA palavra informada é um palíndromo!")
    else:
        print("\nA palavra informada não é um palíndromo!")

    if input("\nDeseja informar outra palavra (S/N)? Resp: ") != 's':
        print("\nMuito bem! Encerrando o programa...\n")
        time.sleep(1)
        break