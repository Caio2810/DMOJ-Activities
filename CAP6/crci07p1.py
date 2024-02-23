def l_level(y,x1):
    global floor
    for h,s,e in floor:
        if h<y:
            if s<=x1<=e:
                return y-h
    return y
def r_level(y,x2):
    global floor
    for h,s,e in floor:
        if h<y:
            if s<=x2<=e:
                return y-h
    return y




n = int(input())
floor = []
for i in range(n):
    floors = list(map(int,input().split()))
    floor.append([floors[0],floors[1]+1,floors[2]])
floor.sort(reverse = True,key = lambda x:x[0])
stare = 0
for y,x1,x2 in floor:
    stare+= l_level(y,x1) + r_level(y,x2)
print(stare)