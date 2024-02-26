dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

N, M = map(int,input().split())

ans = 0

grid = [list(input()) for i in range(N)]

def in_range(x,y):
    return 0<=x<N and 0<=y<M

for x in range(N):
    for y in range(M):
        if grid[x][y] =='L':

            for dx, dy in zip(dxs,dys):
                nx, ny = x+dx, y+dy
                if in_range(nx,ny) and grid[nx][ny] == 'E':
                    nnx, nny = nx+dx, ny+dy
                    if in_range(nnx,nny) and grid[nnx][nny] == 'E':
                        ans += 1

print(ans)