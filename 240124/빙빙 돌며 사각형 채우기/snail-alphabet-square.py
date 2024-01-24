n, m = map(int,input().split())

grid = [[-1]*m for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
x, y = 0, 0
direct = 0

grid[0][0] = 0

for i in range(1,n*m):
    nx = x + dxs[direct]
    ny = y + dys[direct]
    if not in_range(nx,ny) or grid[nx][ny] != -1:
        direct = (direct + 1) % 4

    x = x + dxs[direct]
    y = y + dys[direct]
    grid[x][y] = i

for i in range(n):
    for j in range(m):
        print(chr((grid[i][j]%26)+65),end=' ')
    print()