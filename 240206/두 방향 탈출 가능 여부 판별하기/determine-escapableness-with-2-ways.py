grid = []
visited = []
dxs = [1,0]
dys = [0,1]
ans = 0
###################
def dfs(x,y):
    global visited,ans

    for dx, dy in zip(dxs,dys):
        nx = x+dx
        ny = y+dy
        if can_go(nx,ny):
            visited[nx][ny] = 1
            dfs(nx,ny)
    return

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y] == 0:
        return False
    if visited[x][y]:
        return False
    return True

def in_range(x,y):
    return 0<=x<N and 0<=y<M
###################
N, M = map(int,input().split())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([False for i in range(M)])

visited[0][0] = True
dfs(0,0)

if visited[N-1][M-1] : 
    print(1)
else: 
    print(0)