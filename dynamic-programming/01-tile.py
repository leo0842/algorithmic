tile = dict()
tile[1] = 1
tile[2] = 2

N = int(input())
for i in range(3, N+1):
    tile[i] = (tile[i-2] + tile[i-1])%15746

print(tile[N])