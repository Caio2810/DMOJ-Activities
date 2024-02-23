def encontrar_desistente():
    n = int(input())
    inscritos = set()
    contador = {}

    for _ in range(n):
        inscrito = input().strip()
        inscritos.add(inscrito)
        contador[inscrito] = contador.get(inscrito, 0) + 1

    for _ in range(n - 1):
        completo = input().strip()
        contador[completo] += 1

    for nome, contagem in contador.items():
        if contagem % 2 == 1:
            return nome

# Identificar o competidor que não completou a corrida
resultado = encontrar_desistente()
print(resultado)
