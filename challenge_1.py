# Version Comparator

def comparar_versoes (v1,v2):
    # 1. Separar por Ponto
    lista1 = v1.split(".")
    lista2 = v2.split(".")

    lista1 = [int(x) for x in lista1]
    lista2 = [int(x) for x in lista2]

    tamanho_max = max(len(lista1,), len(lista2))

    while len(lista1) < tamanho_max:
        lista1.append(0)
    while len(lista2) < tamanho_max:
        lista2.append(0)


    for i in range(tamanho_max):
        if lista1[i] > lista2[i]:
            return 1
        elif lista1[i] < lista2[i]:
            return -1
    
    return 0

#print(comparar_versoes("1.2.0" , "1.1.9")) # 1
#print(comparar_versoes("1.0" , "1.0.0")) # 0 
#print(comparar_versoes("2.0" , "2.1")) #-1





def validar_versao(v):
    partes = v.split(".")
    return all(p.isdigit() for p in partes)


while True:
    v1 = input("Digite a versão 1: ")
    if validar_versao(v1):
        break
    print("Formato inválido! Use algo como 1.2.0")


while True:
    v2 = input("Digite a versão 2: ")
    if validar_versao(v2):
        break
    print("Formato inválido!")


resultado = comparar_versoes(v1, v2)

if resultado == 1:
    print("A versão 1 é a mais recente")
elif resultado == -1:
    print("A versão 2 é a mais recente")
else:
    print("As versões são iguais")