P = int(input())
B = int(input())
D = int(input())


num_badges = P // B


total = num_badges * D + min(P % B, B)

print(total)
