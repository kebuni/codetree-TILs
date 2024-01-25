N = int(input())

grid = []

for i in range(N):
    grid.append(list(map(int,input().split())))

def get_coin(x,y):

    coin = 0

    for i in range(3):
        for j in range(3):
            coin = coin + grid[x+i][y+j]

    return coin

max = -1

for i in range(N-2):
    for j in range(N-2):
        cur = get_coin(i,j)
        if cur > max:
            max = cur

print(max)