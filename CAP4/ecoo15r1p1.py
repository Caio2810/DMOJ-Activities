colors = {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "green": 0,
    "blue": 0,
    "pink": 0,
    "violet": 0,
    "brown": 0
}

numCases = 10

for _ in range(numCases):
    color = input()
    while color != "end of box":
        colors[color] += 1
        color = input()
    
    time = 0
    time += colors["red"] * 16
    colors["red"] = 0
    
    for c in colors:
        time += colors[c] // 7 * 13
        if colors[c] % 7 > 0:
            time += 13
        colors[c] = 0
    
    print(time)

