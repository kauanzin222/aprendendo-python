import random
import time

recorde = float('inf')
contTenta = 0


def verifAcerto (tent, sort):
     if tent == sort:
        return 0
     elif sort > tent:
        return 1
     elif sort < tent:
        return 2
     
while True:

    contTenta = 0
    print("Sorteando número....\n")
    time.sleep(1)
    numSort = random.randint(1, 100)
    

    while True:

        
        while True:
            try:
                numTenta = int(input("Tente adivinhar um número entre 1 a 100: \n"))
        
                if numTenta < 1 or numTenta > 100:
                    print("Número não está entre 1 a 100! Tente novamente.\n")
                    continue

                contTenta += 1
                result = [f"_Você acertou! Você precisou de {contTenta} tentativas! Parabéns.\n", "_O número sorteado é maior!\n", "_O número sorteado é menor!\n"]
                print(result[verifAcerto(numTenta, numSort)])
                break

            except ValueError:
              print("Número inválido! Tente novamente.")
               
        if verifAcerto(numTenta, numSort) != 0 and input("Continuar a tentar (S/N)?\n").lower() != 's':
            print(f"O número sorteado era: {numSort}!\nVocê tentou {contTenta} vezes.")
            if input("Deseja sortear outro número (S/N)?\n").lower() != 's':
                print("Encerrando programa...")

        elif verifAcerto(numTenta, numSort) == 0:
            if contTenta < recorde:
                 recorde = contTenta
            if input("Deseja sortear outro número (S/N)?\n").lower() != 's':
                print(f'Muito bem! Seu recorde foi de {recorde} tentativas!\n')
                print("Encerrando programa...")
                exit()
        