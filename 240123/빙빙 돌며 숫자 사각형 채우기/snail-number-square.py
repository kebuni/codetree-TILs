dxs = [0,1,0,-1]
dys = [1,0,-1,0]
direction = 0
x,y = 0,0

n, m = map(int,input().split())

def in_range(x,y):
    return 0<=x<n and 0<=y<m

grid = [[0]*m for j in range(n)]

grid[0][0] = 1

for i in range(2,n*m+1):
    nx = x + dxs[direction]
    ny = y + dys[direction]

    if in_range(nx,ny) == False or grid[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx = x + dxs[direction]
        ny = y + dys[direction]

    x = nx
    y = ny
    #print(x,y)
    grid[x][y] = i

for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()