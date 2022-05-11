n = int(input())
locs = []
for i in range(n):
    tmp = input().split()
    tmp = list(map(int,tmp))
    locs.extend([tmp])

for i in range(n):
    if locs[i][1] == locs[i][0]:
        tmp = ass[i][0]
        if tmp%2 == 0:
            print(tmp*2)
        else:
            print(tmp*2-1)
    elif locs[i][1] == locs[i][0]-2:
        tmp = locs[i][0]
        if tmp%2 == 0:
            print(tmp*2-2)
        else:
            print(tmp*2-3)
    else:
        print('-1')
