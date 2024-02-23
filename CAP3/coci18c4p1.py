def resultado_cetro(feiticeiro_inicial, duelos):
    feiticeiro_atual = feiticeiro_inicial
    feiticeiros_obedecidos = set()

    for duelo in duelos:
        vencedor, perdedor = duelo
        if feiticeiro_atual == perdedor:
            feiticeiro_atual = vencedor
        feiticeiros_obedecidos.add(feiticeiro_atual)

    return feiticeiro_atual, len(feiticeiros_obedecidos)

feiticeiro_inicial = input().strip()
N = int(input().strip())

duelos = []
for _ in range(N):
    duelo = input().strip().split()
    duelos.append((duelo[0], duelo[1]))

resultado1, resultado2 = resultado_cetro(feiticeiro_inicial, duelos)
print(resultado1)
print(resultado2)
