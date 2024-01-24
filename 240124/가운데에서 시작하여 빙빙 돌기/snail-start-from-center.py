dxs = [0,-1,0,1]
dys = [1,0,-1,0]

n = int(input())

x, y = n//2, n//2
direct = 0
total_dist = 1
dist = total_dist
cur = 1

grid = [[-1]*n for _ in range(n)]
grid[x][y] = cur

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(2,n*n+1):

    x = x + dxs[direct]
    y = y + dys[direct]
    grid[x][y] = i
    dist = dist - 1

    if dist == 0: # 방향 바꾸기. 만약 dist 늘려야 하면 늘려야함
        direct = (direct + 1) % 4
        if direct % 2 == 0:
            total_dist = total_dist + 1
        dist = total_dist

for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()