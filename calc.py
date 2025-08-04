execMain = True

ordem = ["primeiro", "segundo"]
num = [0,0]

def calcula (x, y, op):
    if op == 1:
        return x + y
    elif op == 2:
        return x - y
    elif op == 3:
        return x * y
    elif op == 4 and y == 0:
        return 'Erro: Divisão por Zero!'
    else:
        return x / y
 
while execMain:
    x = 0
    while x < 2:
        try:
            num[x] = float(input(f'\nInsira o {ordem[x]} número: '))
            x += 1
        except ValueError:
            print("Número inválido! Tente novamente.\n")
    
    print("\nOperações disponíveis:\n")
    print("1. Soma (+)\n2. Subtração (-)\n3. Multiplicação (*)\n4. Divisão (/)\n") 
    
    while True:
        try:           
            operacao = int(input("Informe a operação desejada: "))
            break
        except ValueError:    
           print("Número inválido! Tente novamente.\n")

    print(f"Resultado: {calcula(num[0], num[1], operacao)}\n")
    
    if input("Deseja realizar uma nova operação (S/N)?\n").lower() != 's':
        execMain = False
    

    

   