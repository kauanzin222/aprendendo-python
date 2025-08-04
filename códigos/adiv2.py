import random
import time
import numpy as np

recorde = np.zeros((1,3))
contTenta = 0
jogar_adiv = True

def verifAcerto (tent, sort):
     if tent == sort:
        return 0
     elif sort > tent:
        return 1
     elif sort < tent:
        return 2
     
while jogar_adiv:

    print("\nBem-vindo ao jogo de adivinhação! Escolha a dificuldade:")

    reg_dificuldade = [100, 1000, 10000]
    string_dificuldade = ["Fácil", "Médio", "Difícil"]

    escolha = int(input("\n(1) Fácil\n(2) Médio\n(3) Difícil\n"))-1
    contTenta = 0

    print("\nSorteando número....\n")
    time.sleep(1)
    numSort = random.randint(1, reg_dificuldade[escolha])
    

    while True:

        
        while True:
            try:
                numTenta = int(input(f"Tente adivinhar um número entre 1 a {reg_dificuldade[escolha]}: \n"))
        
                if numTenta < 1 or numTenta > reg_dificuldade[escolha]:
                    print(f"Número não está entre 1 a {reg_dificuldade[escolha]}! Tente novamente.\n")
                    continue

                contTenta += 1

                result = [f"_Você acertou! Você precisou de {contTenta} tentativa(s)! Parabéns.\n", 
                          "_O número sorteado é maior!\n", 
                          "_O número sorteado é menor!\n"
                          ]
                
                tentiva = verifAcerto(numTenta, numSort)
                print(result[tentiva])
                break

            except ValueError:
              print("Número inválido! Tente novamente.")
               
        if tentiva != 0 and input("Continuar a tentar (S/N)?\n").lower() != 's':
            print(f"O número sorteado era: {numSort}!\nVocê tentou {contTenta} veze(s).")
            if input("Deseja sortear outro número (S/N)?\n").lower() != 's':
                print("Encerrando programa...")
                jogar_adiv = False
                break

        elif tentiva == 0:
            if contTenta < recorde[0, escolha]:
                 recorde[0, escolha] = contTenta
            if input("Deseja sortear outro número (S/N)?\n").lower() != 's':
                print(f'Muito bem! Seu recorde foi de {recorde} tentativa(s) na dificuldade {string_dificuldade[escolha]}!\n')
                print("Encerrando programa...")
                jogar_adiv = False
                break
        