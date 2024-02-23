import sys

n = int(input())
l = 0
s = 0
line = input()
while line != "EOF":
    if line == "TAKE":
        n += 1
        l += 1
        if n > 999:
            n = 1
    elif line == "SERVE":
        s += 1
    elif line == "CLOSE":
        print(l, l - s, n)
        l = 0
        s = 0
    line = input()

