def main():
    num_camisetas, num_eventos, num_dias = map(int, input().split())
    eventos = list(map(int, input().split()))

    sujeira_camisetas = 0
    lavagens = 0

    for i in range(1, num_dias + 1):
        if sujeira_camisetas == num_camisetas:
            lavagens += 1
            sujeira_camisetas = 0

        num_camisetas += eventos.count(i)
        sujeira_camisetas += 1

    print(lavagens)

if __name__ == "__main__":
    for _ in range(10):
        main()
