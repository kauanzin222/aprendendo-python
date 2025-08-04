main = True

def verif_grau(grau):
    letra = '°'
    grau = grau.lower().replace(' ', '')
    for c in grau:
        if c.isalpha():
            letra += c
            if not(c == 'c' or c == 'k' or c == 'f'):
                return False
            
    sobra = grau.replace(letra, '')

    try:
        float(sobra)
        if sobra != '':
            return True
        
    except ValueError:
        return False
    
def convertor_grau(grau, nova_medida):
    for c in grau:
        if c.isalpha():
            atual_medida = '°' + c
           
    grau = grau.replace(atual_medida,'')
    atual_medida = atual_medida.replace('°', '')

    if nova_medida == 1:
        return str(round(convert_celsius(grau, atual_medida), 2)) + '°C'
    elif nova_medida == 2:
        return str(round(convert_fahr(grau, atual_medida), 2)) + '°F'
    elif nova_medida == 3:
        return str(round(convert_kelvin(grau, atual_medida), 2)) + '°K'

def convert_celsius(grau, atual_medida):
    grau = float(grau)
    if atual_medida.lower() == 'k':
        return grau - 273.15
    else:
        return (grau * 9/5) + 32

def convert_fahr(grau, atual_medida):
    grau = float(grau)
    if atual_medida.lower() == 'c':
        return (grau * 9/5) + 32
    elif atual_medida.lower() == 'k':
        return (grau - 273.15) * 9/5 + 32
    
def convert_kelvin(grau, atual_medida):
    grau = float(grau)
    if atual_medida.lower() == 'c':
        return grau + 273.15
    else:
        return (grau * 9/5) - 459.67

    
            
        
while main:

    while True:
        grauAtual = input("\nInsira o grau atual, especificando com °C, °F ou °K: ")
        
        if not(verif_grau(grauAtual)):
            print("\nGrau inválido! Insira novamente.")
            continue
        else:
            break

    print("\nInforme a medida desejada:")
    while True:
        novaMedida = int(input("\n(1). Celsius\n(2). Fahrenheit\n(3). Kelvin\nDigite aqui: "))

        if novaMedida >= 1 and novaMedida <= 3:
            break
        else:
            print("\nNúmero inválido! Tente novamente.")
            

    novoGrau = convertor_grau(grauAtual, novaMedida)
    print(f"\nO resultado da conversão é: {novoGrau}")

    if input("\nDeseja fazer uma nova conversão (S/N)? ").lower() != 's':
        print("\nMuito bem! Encerrando o programa...\n")