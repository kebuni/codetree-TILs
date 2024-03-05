N, M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
visited = [[False for j in range(M)] for i in range(N)]
ans = 0

def in_range(x,y):
    return 0<=x<N and 0<=y<M 

def choose(x,y,n,value):
    global ans
    if n == 3:
        ans = max(ans,value)
        return

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            choose(nx, ny, n+1, value + grid[nx][ny])
            visited[nx][ny] = False

    return

for x in range(N):
    for y in range(M):
        choose(x,y,0,0)

print(ans)