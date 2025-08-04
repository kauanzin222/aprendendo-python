import random

criar_senha = True

def randomSenha(tamanho):

    letras_minúsculas = "abcdefghijklmnopqrstuvwxyz"
    letras_maiúsculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    especiais = "!@#$%&*"
    caracter_extra = f"{random.choice(letras_maiúsculas)}{random.choice(letras_minúsculas)}{random.choice(especiais)}{str(random.randint(0, 9))}"

    senha = [tamanho] 
    senha = caracter_extra
    if tamanho != 4:
        for x in range(tamanho - 4):
            senha += random.choice(caracter_extra)

    return senha


while criar_senha:
    
    while True:
        try:
            tamSenha = int(input("\nInforme o tamanho da senha desejada (mínimo 4): "))
            if tamSenha < 4:
                print("\nTamanho inválido! Tente novamente.")
                continue
            else:    
                break

        except ValueError: 
            print("\nTamanho inválido! Tente novamente.")
    
    print(f"\nSua nova senha é: {randomSenha(tamSenha)}")

    if input("\nDeseja gerar uma nova senha (S/N)? Digite aqui: ").lower() != 's':
        criar_senha = False
        break


    

