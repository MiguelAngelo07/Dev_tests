 # Simulador de Download
import time
import random

def simulador_download():
    progress = 0

    while progress < 100:
        time.sleep(0.2)  # Simula o tempo

        if random.random() < 0.1:
            print("Falha no download!")
            return False

        progress += random.randint(5,15)

        if progress > 100:
            progress = 100

        print(f"Download: {progress}%")
    
    print("Download Concluído!")
    return True

simulador_download()

def executar_com_retry(func, tentativas=3):
    for tentativa in range(1, tentativas + 1):
        print(f"Tentativa {tentativas}...")

        sucesso = func()

        if sucesso:
            return True
        
        print("tentando novamente...\n")

    print(" Falha após várias tentativas.")
    return False

executar_com_retry(simulador_download, tentativas=3)