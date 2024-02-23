for _ in range(10):
    T, N = map(int, input().split())
    dias_de_atraso = 0

    for dias in range(1, N + 1):
        c = input().strip()
        if c == 'B':
            if dias > dias_de_atraso:
                dias_de_atraso = dias + T - 1
            else:
                dias_de_atraso += T

    print(max(0, dias_de_atraso - N))
