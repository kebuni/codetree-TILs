n, m = map(int,input().split())

dxs = [1,0,-1,0]
dys = [0,1,0,-1]
direct = 0
x,y =0,0

def in_range(x,y):
    return 0<=x<n and 0<=y<m

grid = [[0]*m for i in range(n)]

grid[0][0] = 1

for i in range(2,n*m+1):
    nx = x + dxs[direct]
    ny = y + dys[direct]
    if not in_range(nx,ny) or grid[nx][ny] != 0:
        direct = (direct + 1) % 4
    x = x + dxs[direct]
    y = y + dys[direct]

    grid[x][y] = i

for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()