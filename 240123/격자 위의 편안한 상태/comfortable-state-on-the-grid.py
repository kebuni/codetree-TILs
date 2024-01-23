N, M = map(int,input().split())

grid = [[0]*N for _ in range(N)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def comfortable(x,y):
    cnt = 0
    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx,ny) and grid[nx][ny] == 1:
            cnt = cnt + 1
    return cnt

for _ in range(M):
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1

    grid[r][c] = 1

    if comfortable(r,c) == 3:
        print(1)
    else:
        print(0)