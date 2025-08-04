import time
main = True

tipoMedida = ["Celsius", "Fahrenheit", "Kelvin"]
while main:

    print("\nInicializando convertor.")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")

    print("\nInforme a medida atual:")
    while True:
        try:
            medidaAtual = int(input("\n(1). Celsius\n(2). Fahrenheit\n(3). Kelvin\n"))-1
            break
        except ValueError:
            print("\nNúmero inválido! Tente novamente.")
    
    while True:
        try:
            grauAtual = float(input("\nInforme o grau: ")) 
            break
        except ValueError:
            print("\nGrau informado inválido! Tente novamente.")

    print("\nInforme a medida desejada:")
    while True:
        try:
            novaMedida = int(input("\n(1). Celsius\n(2). Fahrenheit\n(3). Kelvin\n"))-1
            break
        except ValueError:
            print("\nNúmero inválido! Tente novamente.")
    

    result = convertor_graus(grauAtual, medidaAtual)

    print(f"O grau {grauAtual} em {tipoMedida[medidaAtual]} convertido para {tipoMedida[novaMedida]} é: ")

