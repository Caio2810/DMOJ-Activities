def encontrar_modas(numeros):
    contagem = {}
    max_frequencia = 0

    for num in numeros:
        contagem[num] = contagem.get(num, 0) + 1
        max_frequencia = max(max_frequencia, contagem[num])

    modas = [num for num, freq in contagem.items() if freq == max_frequencia]

    return modas

N = int(input())
numeros = list(map(int, input().split()))

modas = encontrar_modas(numeros)

print(" ".join(map(str, sorted(modas))))
